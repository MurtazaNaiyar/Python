#!/bin/bash
name=$RANDOM
$(dask-worker --name $name --memory-limit=16e9 dask-scheduler:8786)