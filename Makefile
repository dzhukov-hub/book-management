runserver:
	python manage.py runserver

celery_worker:
	celery -A config.celery worker -c 1 -l INFO

run_all:
	runserver celery_worker
