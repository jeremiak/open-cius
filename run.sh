#!/bin/bash

mkdir -p /data/clean
mkdir -p /data/downloads
mkdir -p /data/raw

python ./scripts/scrape.py
./scripts/clean.sh
