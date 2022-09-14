.PHONY: clean, build, format, install

clean:
	pipenv run python scripts/clean.py

build: clean
	pipenv run python scripts/build.py

format: clean
	pipenv run python scripts/format.py

install:
	pipenv install -d