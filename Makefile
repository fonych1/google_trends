.PHONY: help docs
.DEFAULT_GOAL := help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install requirements
	pip install -r requirements.txt

reinstall: ## Reinstall requirements
	pip install --upgrade --force-reinstall -r requirements.txt

lock: ## Compile requirements file
	pip-compile --no-header --verbose --output-file requirements.txt requirements.in

upgrade: ## Upgrade requirements file
	pip-compile --no-header --verbose --upgrade --output-file requirements.txt requirements.in