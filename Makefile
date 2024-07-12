
pyenv:
	pyenv virtualenv 3.9.2 django-3.9.2
	pyenv activate django-3.9.2

build:
	make pyenv
	pip3 install -r requirements.txt

start:
	python3 manage.py runserver

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate