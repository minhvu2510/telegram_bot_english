# -*- coding: utf-8 -*-
import random
import api
from settings import *
import Question
import db
from redis import Redis
r = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
# import Question
# print db.get_all_topics()
#
# for i in db.find_by_dict(db.get_all_topics()[0]):
#     print i,type(i),i['key']
# print db.get_total_record(db.get_all_topics()[0])
# mv1 = "\t {} \n A : {} \n B : Người đại diện \n C : Nhàm chán \n D : Vcl".format('Feedback',
#                                                                                                  'Phản hồi',
#                                                                                                  'Người đại diện',
#                                                                                                  'Nhàm chán',
#                                                                                                  'Vcl')
# print mv1
# # ques = Question.question('Feedback', 'Phản hồi', 'Người đại diện', 'Nhàm chán', 'Vcl','Vcl')
# # print ques
# mv = [1,2,3,4,5,6,7]
# random.shuffle(mv)
# # k = db.find_by_dict(db.get_all_topics()[0])
# # print list(k)
# print mv
# k = api.get_question_by_topic('computers')
# for i in k:
#     print i.getAnsA(), type(i)
# print '---------------------------------------------------'
# list_quetions_by_topic = api.get_question_by_topic('conferences')
# print list_quetions_by_topic
# quet = list_quetions_by_topic[1]
# mv1 = "\t {} \n A : {} \n B : {} \n C : {} \n D : {}".format(quet.getquestion(),
#                                                                 quet.getAnsA().encode('utf-8').strip(),
#                                                                 quet.getAnsB().encode('utf-8').strip(),
#                                                                  quet.getAnsC().encode('utf-8').strip(),
#                                                                   quet.getAnswer().encode('utf-8').strip())
# def test():
#     return True,'minhvu'
# print test(),type(test()),test()[0]

# print api.set_forgetful_word('minhvu','deptrai')
# a = api.get_question_by_topic('inventory')
# print a

# b = db.find_by_dict('inventory')
# for i in b:
#     print i
# print db.get_all_keys_redis()
# print api.get_words_forget()
# t = []
# globals()['t'] = [4,2,3,4,5]
def mv():
    global t
    t = [3,2,3,4,5]
mv()
def mv1():
    k = t[0]
    return k
print mv1()
