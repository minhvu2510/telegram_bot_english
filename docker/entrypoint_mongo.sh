#!/bin/bash
set -e
mongorestore -d mvp /mvp
echo "some data for the file" >> /mv.txt
