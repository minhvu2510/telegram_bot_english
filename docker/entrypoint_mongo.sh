#!/bin/sh
set -eu
sleep 15 && mongorestore -d mvp /mvp
docker exec -it mongodb bash -c "mongorestore -d mvp /mvp"
exec mongorestore -d mvp /mvp
mongorestore -d mvp /mvp
echo "second statement" > /file1.txt