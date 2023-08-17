.ONESHELL:

ifeq ($(OS),Windows_NT)
    RENAME_CMD = rename
    RENAME_FLAGS = .env.sample .env
else
    RENAME_CMD = mv
    RENAME_FLAGS = .env.sample .env
endif

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

.PHONY: venv-create local-setup

# local-setup
rename_env_file:
	$(RENAME_CMD) $(RENAME_FLAGS)

venv-create:
	python -m venv venv

local-setup:
	pip install -r requirements_dev.txt && pip install .

# Prefect
prefect-login:
	prefect cloud login --key $(PREFECT_API_KEY)

prefect-logout: prefect-login
	prefect cloud logout

prefect-worker-create: prefect-login
	prefect work-pool create mlops-pool -t process

prefect-worker-start: prefect-login
	prefect worker start -p mlops-pool

prefect-deploy: prefect-login
	prefect project init && prefect deploy --all

prefect-cloud: prefect-login prefect-deploy prefect-worker-start

# Docker
docker-build:
	docker-compose build

docker-run: docker-build
	docker-compose up -d

docker-stop:
	docker-compose down

# Terraform
terraform-init:
	cd infrastructure
	terraform init

terraform-apply:
	cd infrastructure
	terraform apply --var-file=vars/prod.tfvars

terraform-destroy:
	cd infrastructure
	terraform destroy --var-file=vars/prod.tfvars

terraform-deploy: terraform-init terraform-apply

# Stop project
destroy: docker-stop terraform-destroy

# Scripts
web-scrapper:
	python src/scrapper/scrapper.py

train-model:
	python src/training/preprocess.py
	python src/training/train.py

monitoring-model:
	python src/monitoring/monitoring.py

generate-predictions:
	python src/generate_predicts.py

execute-all-pipeline: web-scrapper train-model generate-predictions monitoring-model
