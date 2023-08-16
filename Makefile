.ONESHELL:

# Verifica o sistema operacional para definir os comandos corretos
ifeq ($(OS),Windows_NT)
	VENV_ACTIVATE = venv\Scripts\activate
else
	VENV_ACTIVATE = venv/bin/activate
endif

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

.PHONY: local-setup venv-create

# local-setup
rename_env_file:
	$(RENAME_CMD) $(RENAME_FLAGS)

venv-create:
	python -m venv venv

local-setup: venv-create
	.\$(VENV_ACTIVATE) && pip install -r requirements_dev.txt && python setup.py install

# Prefect
prefect-login:
	prefect cloud login -k $(PREFECT_API_KEY)

prefect-logout:
	prefect cloud logout

prefect-worker-create:
	prefect work-pool create mlops-pool -t process

prefect-worker-start:
	prefect worker start -p mlops-pool

prefect-deploy:
	prefect deploy --all

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

# Scripts
web-scrapper: activate-venv
	python src/scrapper/scrapper.py

train-model: activate-venv
	python src/training/preprocess.py
	python src/training/train.py

monitoring-model: activate-venv
	python src/monitoring/monitoring.py

generate-predictions: activate-venv
	python src/generate_predicts.py

execute-all-pipeline: web-scrapper train-model generate-predictions monitoring-model
