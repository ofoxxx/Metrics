# metrics

A sample Python project for visualizing GitHub analytics.

Adapted from https://graphite.dev/guides/github-analytics-dashboard

## Requirements
- Python 3.11+

## Quickstart

Create a virtual environment, install dependencies, and run tests (using zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -U pip
pip install poetry
poetry install
# Copy .env.example to .env and set your GitHub token
cp .env.example .env
# Run tests using the src package path
PYTHONPATH=src poetry run pytest -q
```

## Run the CLI

The project includes a Dash app for visualizing GitHub analytics. To run the app:

```bash
poetry run python -m metrics
```

The app provides a dashboard with visualizations such as:
- Commits per day

Navigate to `http://127.0.0.1:8050/` in your browser to view the app.

## Project Layout

- `src/metrics` - package source
- `tests` - pytest tests
- `pyproject.toml` - project metadata

## License

MIT
