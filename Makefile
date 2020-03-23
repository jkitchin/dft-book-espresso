

html:
	jupyter nbconvert *.ipynb --output-dir docs
	git add docs
	git commit  -m "publishing docs"
	git push
