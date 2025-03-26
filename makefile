.PHONY: help install migrate run clean

help:
	@echo "Makefile команди:"
	@echo "  make install  - Встановити залежності"
	@echo "  make migrate  - Виконати міграції"
	@echo "	 make test     - Виконати тести"
	@echo "  make run      - Запустити сервер"

venv:
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip

install: venv
	. venv/bin/activate && pip install -r requirements.txt

migrate:
	. venv/bin/activate && python manage.py makemigrations && python manage.py migrate || echo "Migration failed"

test:

	.venv/bin/activate && python manage.py test

run:
	. venv/bin/activate && python manage.py runserver
