#!/usr/bin/env bash
/usr/local/bin/docker-compose -f /var/test_deployment/docker-compose-prod.yml up --scale dask-worker=4 -d
