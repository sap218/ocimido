#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:57:12 2019
@author: samantha

ALL results from every post/comment
"""

#------------------- importing modules
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy as np

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
from nltk import ngrams

###########################################################

file = "output.csv"
df = pd.read_csv(file)

x = 0
for item in range(16):
    df = df.drop((str(item) + "/post_date"), axis=1)
    df = df.drop((str(item) + "/topic_id"), axis=1)
    df = df.drop((str(item) + "/user_link"), axis=1)
    df = df.drop((str(item) + "/user_name"), axis=1)
    df = df.drop((str(item) + "/topic_title"), axis=1) ## BLAH
    x = x+1

columns = []
for row in df.iterrows():
    index, data = row
    columns.append(data.tolist())

flat_list = [str(item).lower() for sublist in columns for item in sublist]
flat_list = [x for x in flat_list if str(x) != 'nan']


column_split = []
for item in flat_list:
    column_split.append(item.split())

flat_list = [str(item).lower() for sublist in column_split for item in sublist] # POSTS ONLY 

###########################################################

df = pd.read_csv(file)
column = list(df['0/topic_title'])
column_split = []
for item in column:
    column_split.append(item.split())
flat_list2 = [item.lower() for sublist in column_split for item in sublist]


flat_list3 = flat_list + flat_list2 # combining posts and topic titles

###########################################################
###########################################################
###########################################################


flat_list3 = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in flat_list3] # removing special chars
flat_list4 = [x for x in flat_list3 if x] # removing empty items

flat_list5 = flat_list4
string = ' '.join(map(str, flat_list5))

###########################################################
###########################################################

# removing stop words - a/the/this
stopWords = set(stopwords.words('english'))
words = word_tokenize(string)
wordsFiltered = [] # removing stop words
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

###########################################################

stemming = [] # shorten words
ps = PorterStemmer()
for w in wordsFiltered:
    stemming.append(ps.stem(w))

stemmed = [] # shorten words
ps = PorterStemmer()
for w in stemming:
    stemmed.append(ps.stem(w))

###########################################################
###########################################################
###########################################################

all_words = dict(Counter(stemmed))
words = {k: v for k, v in all_words.items() if v > 60} 

bad_ones = ['1', '2', '3', '4', '5', '6','8','10',
        'abl', 'advic','ago','alreadi','also','although','alway','anoth','answer','anyth','around','ask','actual','anyway','ayliff',
        'becca','becom','bristol','believ',
        'call','cant','caron','child','children','christma','come','could','came','consid','chanc','contact',
        'daughter','day','didnt','discuss','doesnt','dont','dr','difficult','decid',
        'enough','ever','everi','everyon','everyth','etc','earli','especi','expect',
        'follow','fine','free','friend','forward',
        'get','give','given','go','goe','got','gone','gener',
        'happen','happi','help','hi','hope','howev','hello','havent','he',
        'id','idea','ill','im','inform','ive','isnt','info',
        'jack','jia','j',
        'keep','know','kid',
        'last','let','like','link','lot','love','luck','least','later','low','local',
        'made','make','mani','maxidex','may','mean','mention','methotrex','might','month','much','moment','moorfield','mind',
        'need','never','new','news','next','nicki','noth','notic','nice','nur','nh',
        'ok','old','olivia','other','owen','offer',
        'peopl','point','posit','possibl','problem','prof','put','place','parent','person','probabl','privat','pretti',
        'question','quit','quiet',
        'read','realli','riley','reason','recent','rather','regard',
        'said','say','school','seem','seen','sinc','someth','son','soon','sorri','sound','stay','still','stop','sure','sarah','someon','sometim','she','saw','sort','sam','stori','suggest','speak','sherri',
        'talk','tell','thank','that','thing','think','though','thought','told','today','tomorrow','tri','turn',
        'understand','us','use','updat','usual','u',
        'visit',
        'wait','want','way','week','well','went','whether','wish','wor','wont','what','wasnt','without','wonder','work','worri','would','worth','websit',
        'x','xx',
        'ye','yet','your','youv','yesterday','year',
        ]
for item in bad_ones:
    del words[item]

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 35
fig_size[1] = 17
plt.rcParams["figure.figsize"] = fig_size

import seaborn as sns
data = pd.DataFrame(list(words.items()), columns=['word', 'count'])
data = data.sort_values('count')
plt.figure(1)
sns.barplot("word", "count", data=data)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.savefig("plots/ALL.png")

###########################################################
###########################################################

string = ' '.join(map(str, stemmed)) # NGRAMS
bad_ones = ['hi','edit','dont','know','fort','finger','back','nicki','sure','luck','next','maxin','tania',
            'news','post','like','hope','wish','thank','sorri','becca','thank','anyon','realli','daughter',
            'glad','everi','though','might','keep','olivia','plea','someth','would','goe','hate','william',
            'mistrust','penyebab','dedic','gejala','inform','wont','darah','read','tinggi','asam','websit']
for item in bad_ones:
    string = string.replace(item, '')
n = int(input("NGRAM\t(2 / 3):\t\t"))
#n = 3
sixgrams = ngrams(string.split(), n)
ngrams = []
for grams in sixgrams:
  ngrams.append(grams)
ngrams = dict(Counter(ngrams))
if n == 2:
    ngrams = {k: v for k, v in ngrams.items() if v > 20}
elif n == 3:
    ngrams = {k: v for k, v in ngrams.items() if v > 5}

ngrams = pd.DataFrame(list(ngrams.items()), columns=['combinations', 'count'])
ngrams = ngrams.sort_values('count')
#print(ngrams)
plt.figure(2)
sns.barplot("combinations", "count", data=ngrams)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.savefig("plots/ALL_ngrams_%s.png" % (n))