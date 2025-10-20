#!/usr/bin/env bash
set -euo pipefail
set -x

# Build and (optionally) publish the Quarto book in memm_book/
# Usage:
#   ./build_upload.sh           # build and publish
#   ./build_upload.sh --build-only
#   ./build_upload.sh --publish-only
#   ./build_upload.sh --no-venv
#   ./build_upload.sh --clean

PROJECT_DIR="memm_book"
SITE_DIR="$PROJECT_DIR/_site"
VENV_DIR=".venv"
PY_REQS="requirements.txt"

BUILD_ONLY=false
PUBLISH_ONLY=false
NO_VENV=false
CLEAN=false
AUTO_FIX_LINKS=false
QUARTO_OPTS=(--no-cache)

usage(){
	cat <<EOF
Usage: $0 [options]
Options:
	--build-only       Render the Quarto site but do not publish
	--publish-only     Publish the last-built site to gh-pages (skip build)
	--no-venv          Do not create/activate local .venv
	--clean            Remove generated site before building
	--execute          Force executing notebooks during render
	--help             Show this help
EOF
	exit 1
}

while [[ $# -gt 0 ]]; do
	case "$1" in
		--build-only) BUILD_ONLY=true; shift;;
		--publish-only) PUBLISH_ONLY=true; shift;;
		--no-venv) NO_VENV=true; shift;;
		--clean) CLEAN=true; shift;;
		--execute) QUARTO_OPTS=(); QUARTO_OPTS+=(--execute); shift;;
		--auto-fix-links) AUTO_FIX_LINKS=true; shift;;
		--help|-h) usage; shift;;
		*) echo "Unknown option: $1"; usage;;
	esac
done

if [ "$PUBLISH_ONLY" = true ] && [ "$BUILD_ONLY" = true ]; then
	echo "--build-only and --publish-only are mutually exclusive" >&2
	exit 1
fi

if [ ! -d "$PROJECT_DIR" ]; then
	echo "Quarto project directory '$PROJECT_DIR' not found."
	echo "If you haven't migrated yet, run scripts/migrate_to_quarto.py or pass --no-venv to build the legacy Jupyter Book."
	exit 1
fi

if [ "$NO_VENV" = false ]; then
	if [ ! -d "$VENV_DIR" ]; then
		echo "Creating virtualenv in $VENV_DIR"
		python3 -m venv "$VENV_DIR"
	fi
	# shellcheck disable=SC1091
	source "$VENV_DIR/bin/activate"
	pip install --upgrade pip
	# install Python helpers used for migration and book helpers (if present)
	pip install jupytext nbformat pyyaml || true
	# ghp-import is used to publish the static site to gh-pages
	pip install ghp-import || true
fi

if [ "$PUBLISH_ONLY" = false ]; then
	if [ "$CLEAN" = true ]; then
		echo "Cleaning previous site: $SITE_DIR"
		rm -rf "$SITE_DIR"
	fi

	if [ "$AUTO_FIX_LINKS" = true ]; then
		if [ -f scripts/fix_links.py ]; then
			# run the link fixer in non-destructive mode first
			python3 scripts/fix_links.py || true
			# then apply fixes
			python3 scripts/fix_links.py --fix || true
			echo "Applied automatic link fixes (fix_links.py --fix)"
		else
			echo "Link fixer script not found: scripts/fix_links.py"
		fi
	fi

	# Run preflight check and optionally fix missing chapters in _quarto.yml
	if [ -f scripts/preflight_check.py ]; then
		python3 scripts/preflight_check.py --fix-quarto || true
	fi

	if ! command -v quarto >/dev/null 2>&1; then
		echo "Quarto CLI is not installed or not on PATH. Please install Quarto from https://quarto.org"
		[ "$NO_VENV" = false ] && deactivate || true
		exit 1
	fi

	echo "Rendering Quarto book: $PROJECT_DIR"
	# pass through options like --execute/--no-cache by expanding QUARTO_OPTS
	quarto render "$PROJECT_DIR" "${QUARTO_OPTS[@]}"
fi

if [ "$BUILD_ONLY" = false ]; then
	# determine where Quarto wrote the output. try common locations
	CANDIDATES=(
		"$PROJECT_DIR/_site"
		"$PROJECT_DIR/_book"
		"$PROJECT_DIR/_book/_site"
		"$PROJECT_DIR/_site/_book"
	)
	SITE_DIR_FOUND=""
	for c in "${CANDIDATES[@]}"; do
		if [ -d "$c" ]; then
			SITE_DIR_FOUND="$c"
			break
		fi
	done
	if [ -z "$SITE_DIR_FOUND" ]; then
		# fallback: look for an index.html under the project directory
		FOUND_HTML=$(find "$PROJECT_DIR" -maxdepth 3 -type f -name 'index.html' | head -n 1 || true)
		if [ -n "$FOUND_HTML" ]; then
			SITE_DIR_FOUND=$(dirname "$FOUND_HTML")
		fi
	fi
	if [ -z "$SITE_DIR_FOUND" ]; then
		echo "Site directory not found after build. Nothing to publish." >&2
		[ "$NO_VENV" = false ] && deactivate || true
		exit 1
	fi
	SITE_DIR="$SITE_DIR_FOUND"
	echo "Using site directory: $SITE_DIR"

	if ! command -v ghp-import >/dev/null 2>&1; then
		echo "ghp-import not found in PATH. Attempting to install into virtualenv."
		if [ "$NO_VENV" = false ]; then
			pip install ghp-import
		else
			echo "Please install ghp-import (pip install ghp-import) or activate a venv." >&2
			exit 1
		fi
	fi

	echo "Publishing site to gh-pages branch (using ghp-import)"
	ghp-import -n -p -f -m "Publish Quarto site" "$SITE_DIR"
fi

# deactivate venv if we activated it
if [ "$NO_VENV" = false ]; then
	deactivate || true
fi

echo "Done."