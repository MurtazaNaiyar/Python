#!/usr/bin/env bash
docker build --rm --build-arg \
  PYTHON_DEPS="\
  	pyxlsb \
  	xlrd \
  	botocore==1.9.7 \
  	boto==2.48.0 \
  	boto3==1.6.7 \
  	s3fs==0.1.4 \
  	s3transfer==0.1.13 \
  	pandas_redshift \
  	psycopg2==2.7.4 \
  	psycopg2-binary==2.7.4 \
  	sqlalchemy_redshift \
  	texttable \
  	rpyc" \
  -t puckel/docker-airflow .
