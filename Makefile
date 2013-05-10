clean:
	@find . -iname '*.pyc' -delete
	@rm -rf dist/ django_thumbor.egg-info/
test: clean
	@./manage.py test
install:
	@pip install -r dev_requirements.txt
release: clean
	@python setup.py -q sdist upload -r pyorg
