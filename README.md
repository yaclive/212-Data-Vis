# 212-Data-Vis

## Steps to run after clone
- python -m venv env
- env\Scripts\activate
- pip install flask

- set FLASK_APP=run.py
- set FLASK_DEBUG=1

- python -m flask run

## Steps to run there after
- env\Scripts\activate

- set FLASK_APP=run.py
- set FLASK_DEBUG=1

- python -m flask run

## TO-DO / Improvements / Optimisations
- Render signal lines at load time into svg
- Only respond to left click
- Add more datasets
- Experiment with time scrubbing padding, time += (cursor.x - time) / 2
