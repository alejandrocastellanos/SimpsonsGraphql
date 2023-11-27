#!/usr/bin/env bash

gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8190 simpsons:app
