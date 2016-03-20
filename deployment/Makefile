PROJECT_ID := qgissharing

SHELL := /bin/bash


# ----------------------------------------------------------------------------
#    C O M M A N D S
# ----------------------------------------------------------------------------
status:
	@echo
	@echo "-------------------------------------------------------------------"
	@echo "Status of all running staging containers"
	@echo "-------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) ps

run: build web migrate collectstatic

deploy: run superuser
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Bringing up fresh staging instance "
	@echo "You can access it on http://localhost:61201"
	@echo "------------------------------------------------------------------"

build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) build

web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d web

migrate:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running migrate static in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py	migrate

collectstatic:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Collecting static in staging mode"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)_uwsgi_1 python manage.py collectstatic --noinput

superuser:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating a superuser in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi python manage.py createsuperuser

loaddata:
	@echo
	@echo "-------------------------------------------------------------------"
	@echo "Load specified fixture"
	@echo "-------------------------------------------------------------------"
	@read -p "Enter the fixture:" fixture; \
	docker-compose -p $(PROJECT_ID) run uwsgi python manage.py loaddata $$fixture

kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) kill

rm: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing staging instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) rm

logs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing uwsgi logs in staging mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) logs uwsgi

weblogs:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Showing web logs"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) logs web

shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) run uwsgi /bin/bash

dbshell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling"
	@echo "------------------------------------------------------------------"
	@docker exec -t -i $(PROJECT_ID)_db_1 psql -U docker -h localhost postgres
