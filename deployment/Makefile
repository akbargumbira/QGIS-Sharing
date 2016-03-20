PROJECT_ID := qgis-sharing

SHELL := /bin/bash


# ----------------------------------------------------------------------------
#    D E V E L O P M E N T S    C O M M A N D S
# ----------------------------------------------------------------------------
dev-deploy: dev-build dev-run dev-superuser

dev-run: dev-web dev-makemigrations dev-migrate

dev-status:
	@echo
	@echo "-------------------------------------------------------------------"
	@echo "Status of all running development containers"
	@echo "-------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) ps

dev-build:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building dev"
	@echo "------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) build

dev-web:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Running web dev mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) up -d devweb

dev-shell:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Shelling in in dev"
	@echo "------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) run devweb python manage.py shell

dev-makemigrations:
	@echo
	@echo "-------------------------------------------------------------------"
	@echo "Run makemigrations"
	@echo "-------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) run devweb python manage.py makemigrations

dev-migrate:
	@echo
	@echo "-------------------------------------------------------------------"
	@echo "Run migrate"
	@echo "-------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) run devweb python manage.py migrate

dev-superuser:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Creating a superuser in development mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) run devweb python manage.py createsuperuser

dev-kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing dev"
	@echo "------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) kill

dev-rm: dev-kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing dev! "
	@echo "------------------------------------------------------------------"
	@docker-compose -p dev-$(PROJECT_ID) rm
