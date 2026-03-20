#!/bin/bash

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
echo "To start the env run source ./venv/bin/activate"
