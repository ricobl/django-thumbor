BUMP := 'patch'

clean:
	@find . -iname '*.pyc' -delete  # py2
	@find . -iname '__pycache__' -delete  # py3
	@rm -rf dist/ django_thumbor.egg-info/

run: clean
	@pipenv run ./manage.py runserver

test: clean
	@pipenv run ./manage.py test -v 2

django_shell: clean
	@pipenv run ./manage.py shell

shell: clean
	@pipenv shell

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

setup_build:
	@pipenv run pip install twine build

build: clean
	@pipenv run python -m build

upload_test: build
	@pipenv run twine upload -r testpypi dist/*

release: build
	@pipenv run twine upload -r django-thumbor dist/*
