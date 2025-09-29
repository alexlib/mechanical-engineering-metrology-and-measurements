@echo off
REM Activate the mdd environment
call .venv\Scripts\activate

REM Build the Jupyter book
jupyter-book build book

REM Update GitHub Pages
ghp-import -n -p -f book/_build/html

REM Deactivate the environment
call deactivate