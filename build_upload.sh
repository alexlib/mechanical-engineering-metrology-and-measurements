# use mdd environment
# edm shell -e mdd
# or 
# conda activate mdd
jupyter book build --html
ghp-import -n -p -f _build/html