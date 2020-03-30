#!/bin/bash

echo "Starting Flask..."

source ./venv/bin/activate
flask run &>/tmp/flask.log
