#!/usr/bin/env bash
set -ex

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
