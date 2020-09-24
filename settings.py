#!/usr/bin/python
# -*- coding: utf8 -*-
# vunm

import os


# RabbitMQ
MONGO_CLIENT = os.getenv('MONGO_CLIENT', 'mongodb://localhost:27017/')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'mvp')
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
TOKEN  = os.getenv('TOKEN', '834857847:AAH-_g84YhfoYW5Oc60Kaaaaaaaaaa')
REDIS_DB = 5
REDIS_DB_LOG = 21