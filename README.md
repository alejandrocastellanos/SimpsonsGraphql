![alt logo](logo.png)

# SimpsonsGraphql


The Simpsons API, information by character and random famous quote

## API Reference
Run

`python main.py`

Then

Full documentation http://0.0.0.0:8190/graphql

## Running Tests

Run all tests with

```bash
pytest -s -vvvv
```

Check this for more information on using pytest.

## Pre-Commit

### Installation
`pip install pre-commit`

### Add a pre-commit configuration
If `.pre-commit-config.yaml` file exist.

Run: `pre-commit install`

### (optional) Run against all the files
it's usually a good idea to run the hooks against all of the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks).

Run: `pre-commit run --all-files`

#### pre-commit will now run on every commit.


## Poetry

* https://python-poetry.org/docs/basic-usage/

### Installation
`pip install poetry`

### Initialising a pre-existing project

`cd pre-existing-project`

`poetry init`


### Specifying new dependencies

`poetry add pendulum`


## Docker

`docker compose up -d`

## Copyright
Alejandro Castellanos