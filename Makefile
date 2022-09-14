clean:
	pipenv run python scripts/clean.py

build: clean
	pipenv run python scripts/build.py