### /InsightDataScience/anomaly_detection ###
import math
import sys
import copy
import operator
import re
import heapq
import numpy as np
from heapq import *
from operator import itemgetter
from operator import attrgetter
from collections import Counter
import json, ast
from collections import OrderedDict
from bson.json_util import dumps

class User:
    def __init__(self, x):
        self.user_id = x

    def __repr__(self):
        return str(self.user_id)
############################################
def average(s):
    return (sum(s)*1.0)/len(s)

def stdDeviation(s):
    variance = map(lambda x: (x-average(s))**2, s)
    avg_var = average(variance)
    standard_deviation = math.sqrt(avg_var)
    return standard_deviation

def anomaly_calc(s):
    anomalous = average(s) + 3*stdDeviation(s)
    return anomalous
############################################
lines = []
with open('../log_input/batch_log.json') as f:
    lines.extend(f.read().splitlines())
print("batch_log.json: " + str(lines))

lines[0].encode('ascii', 'ignore')

parameters = {}
parameters = json.loads(lines[0]) # json.loads(lines[0])

print(parameters)
D = parameters ['D']
T = parameters['T']
#print(D, T)
#param = parameters.split(',')
#param.replace('"', '')
#print("paramameters :", type(parameters))
#print(parameters['T'])

events = {}
amount_set=[]
for i in range(1, len(lines)):
    events[i]= json.loads(lines[i]) # json.loads(lines[i])
    lines[i].encode('ascii', 'ignore')
    #print("events :", events[i]['event_type'])
    if events[i]['event_type'] == 'purchase':
        amount = events[i]['amount'].encode('ascii', 'ignore')
        amount = float(amount)
        amount_set.append(amount)
        #print(type(amount))
        #print(events[i]['amount'])

L = len(amount_set)
print (amount_set)
# avg = average(amount_set)
# print(avg)
if ( L > 1 and L <= T):
    anom_val = anomaly_calc(amount_set)
    anom_val = round(anom_val, 2)
    print("anomolous purchase: " + str(anom_val))

fw = open('../log_output/flagged_purchases.json', 'w')

stream_lines = []
with open('../log_input/stream_log.json') as fstr:
    stream_lines.extend(fstr.read().splitlines())
print("stream_log.json: " + str(stream_lines))

str_events = {}
#print(type(str_events))
keyorder = ['event_type', 'timestamp', 'id', 'amount', 'mean', 'sd']

itemDict = OrderedDict()

str_amount_set=[]
for i in range(0, len(stream_lines)):
    str_events[i]= json.loads(stream_lines[i])
    stream_lines[i].encode('ascii', 'ignore')
    #print("str_events :", str_events[i]['event_type'])
    if str_events[i]['event_type'] == 'purchase':
        str_amount = str_events[i]['amount'].encode('ascii', 'ignore')
        str_amount = float(str_amount)
        str_amount_set.append(str_amount)
        #print(type(str_amount))
        print(str_events[i]['amount'])
        if str_amount > anom_val:
            #json = dumps(str_events[i])
            str_events[i]['mean'] = average(str_amount_set)
            str_events[i]['sd'] = stdDeviation(str_amount_set)
            str_events[i] = sorted(str_events[i].items(), key=lambda i: keyorder.index(i[0]))
            #final_flag = str(json.dumps(str_events[i]))
#            print(type(final_flag))
            #itemDict = {item[0]: item[1] for item in str_events[i]}
            #d = dict(itertools.izip_longest(*[iter(l)] * 2, fillvalue=""))
            dict_l = OrderedDict(str_events[i])
            #dict_l = json.loads(str_events[i], object_pairs_hook=OrderedDict)
            print(dict_l)
            print json.dumps(dict_l)
            fw.write(json.dumps(dict_l))
            #fw.write(json.dumps(itemDict))
            
# Lstr = len(str_amount_set)
# print (str_amount_set)


'''paramDict = {}  # dictionary

for p in param:
    pair = p.split(':')
    D = pair[0].strip()
    T = pair[1].strip()
    paramDict[D] = int(T)

print("paramDict: ", paramDict.items)'''


