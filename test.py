# -*- coding: utf-8 -*-
import random
import api
from settings import *
import Question
import db
from redis import Redis
r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

