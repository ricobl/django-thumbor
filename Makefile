BUMP := 'patch'

clean:
	@find . -iname '*.pyc' -delete  # py2
	@find . -iname '__pycache__' -delete  # py3
	@rm -rf dist/ django_thumbor.egg-info/

test: clean
	@./manage.py test

install:
	@pip install -r dev_requirements.txt

patch:
	@$(eval BUMP := 'patch')

minor:
	@$(eval BUMP := 'minor')

major:
	@$(eval BUMP := 'major')

bump:
	@bumpversion ${BUMP}

release: clean
	@python setup.py -q sdist upload
