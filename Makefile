setup:
	python3 -m venv venv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt