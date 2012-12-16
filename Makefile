clean:
	@find . -iname '*.pyc' -delete
test: clean
	@./manage.py test
install:
	pip install -e .
