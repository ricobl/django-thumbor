BUMP := 'patch'

clean:
	@find . -iname '*.pyc' -delete  # py2
	@find . -iname '__pycache__' -delete  # py3
	@rm -rf dist/ django_thumbor.egg-info/

run: clean
	@pipenv run ./manage.py runserver

test: clean
	@pipenv run ./manage.py test -v 2

shell: clean
	@pipenv run ./manage.py shell

install:
	@pipenv install --dev

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
