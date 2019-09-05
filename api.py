# -*- coding: utf-8 -*-

import random

from settings import *
import db
import Question
from redis import Redis
r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def get_all_key():
    keys = r.keys()
    return keys

def get_item(key):

    item = r.get(key)
    # print(item.decode('utf-8'))
    return item

def get_data_in_mongo():
    pass

def get_question_by_topic(topic):
    list_vocab = list(db.find_by_dict(topic))
    len_list = db.get_total_record(topic)
    list_result = []
    for i in list_vocab:
        list_answer = []
        question_proper = i['key']
        answer_proper = i['value']
        while len(list_answer) < 3:
            if(answer_proper not in list_answer):
                list_answer.append(list_vocab[random.randint(0,len_list - 1)]['value'])
            else:
                list_answer.remove(answer_proper)
        list_answer.append(answer_proper)
        random.shuffle(list_answer)
        ques = Question.question(question_proper,list_answer[0],list_answer[1],list_answer[2],list_answer[3],answer_proper)
        list_result.append(ques)
    random.shuffle(list_result)
    return list_result

def get_commands_topic():
    list_topics = db.get_all_topics()
    dict = {}
    for i in list_topics:
        if i != 'promotions,pensions,awards' and i != 'note' and i != 'user':
            dict[i] = 'Study by topic '

    return dict
def get_topics():
    return list(db.get_all_topics())

# ----------------------
def set_forgetful_word(key,value,time):
    # 604800
    r.set(key,value,time)

def get_words_forget():
    list_keys = db.get_all_keys_redis()
    list_topics = db.get_all_topics()
    len_list_topics = len(list_topics)
    topic = list_topics[random.randint(0,len_list_topics - 1)]
    find_topic = list(db.find_by_dict(topic))
    list_resutl = []
    for i in list_keys:
        list_answer = []
        key = i
        value = r.get(i)
        print value
        while len(list_answer) < 3:
            if value not in list_answer:
                list_answer.append(find_topic[random.randint(0,len(find_topic) - 1)]['value'])
            else:
                list_answer.remove(value)
        list_answer.append(value)
        random.shuffle(list_answer)
        ques = Question.question(key, list_answer[0], list_answer[1], list_answer[2], list_answer[3],
                                 value)
        list_resutl.append(ques)
    random.shuffle(list_resutl)
    return list_resutl

