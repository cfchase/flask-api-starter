#!/bin/bash

set -x

source secrets

export SECRET_KEY=$SECRET_KEY
export SERVER_PORT=$SERVER_PORT
export FLASK_DEBUG=true

source venv/bin/activate


FILE_NAME="${1:-wsgi.py}"

if [ "$FILE_NAME" == "shell" ]; then
  python
else
  python ${FILE_NAME}
fi