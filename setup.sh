#!/bin/sh
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements/common.txt
pip install -r requirements/linter.txt
pip install -r requirements/custom_local.txt
pre-commit install --install-hooks
