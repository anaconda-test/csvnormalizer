test:
	pip install nose
	nosetests -s  $(tests)

clean:
	find . -name "*~" -type f -delete
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
