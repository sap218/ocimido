#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:09:52 2019
@author: samantha

ALL posts of an individual user
"""

from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 30
fig_size[1] = 15
plt.rcParams["figure.figsize"] = fig_size

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams

import json

#-------------------- importing JSON
def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))
posts = js_r('output.json')

#-------------------- getting list of all users
uid = []
for post in posts:
    for comment in post:
        if "user_link" in comment:
            uid.append(comment["user_link"])

uid = [x for x in uid if x is not None]
uids = dict(Counter(uid))
uids = list(uids)

print("User count:\t 0 -", (len(uids)-1))
u = input("What user do you want to study?:\t")
uid = uids[int(u)] # using this UID

user = uid[-5:]
user = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in user]
user = ''.join(user)
user = user.replace(" ", "")

#-------------------- getting list of comments for particular user
comments = []
for post in posts:
    for comment in post:
        if uid in comment.values():
            if "post_text" in comment:
                comments.append(comment["post_text"])
comments = [item for sublist in comments for item in sublist]
comments = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in comments] # removing special characters
comments = ''.join(comments) # joining 
comments = comments.lower()

#-------------------- stop words
stopWords = set(stopwords.words('english'))
comments = word_tokenize(comments)
wordsFiltered = [] # removing stop words
for item in comments:
    if item not in stopWords:
        wordsFiltered.append(item)

#-------------------- shortening & plotting
stemming = [] 
ps = PorterStemmer()
for item in wordsFiltered:
    stemming.append(ps.stem(item))
string = stemming # FOR NGRAMS

stemming = dict(Counter(stemming))

if len(stemming) > 1000:
    stemming = {k: v for k, v in stemming.items() if v > 50} # if v > 1
else:
    stemming = {k: v for k, v in stemming.items()} 

if len(stemming) > 100:
    stemming = {k: v for k, v in stemming.items() if v > 1} 

stemming = pd.DataFrame(list(stemming.items()), columns=['words', 'count'])
stemming = stemming.sort_values('count')

plt.figure(1)
sns.barplot("words", "count", data=stemming).set_title(user)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.savefig("plots/UID:%s_top-words.png" % (user))

#-------------------- NGRAMS
string = ' '.join(map(str, string)) 

#bad_ones = ['maxin','care','know']
#for item in bad_ones: string = string.replace(item, '')

n = int(input("NGRAM\t(2 / 3):\t\t"))
#n = 2
sixgrams = ngrams(string.split(), n)
ngrams = []
for item in sixgrams:
  ngrams.append(item)
ngrams = dict(Counter(ngrams))

if len(ngrams) > 10000:
    if n == 2:
        ngrams = {k: v for k, v in ngrams.items() if v > 6}
    elif n == 3:
        ngrams = {k: v for k, v in ngrams.items() if v > 4}
    ngrams = pd.DataFrame(list(ngrams.items()), columns=['combinations', 'count'])
    ngrams = ngrams.sort_values('count')
    plt.figure(2)
    sns.barplot("combinations", "count", data=ngrams).set_title(user)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.savefig("plots/UID:%s_ngrams_%s.png" % (user, n))
    
else:
    ngrams = {k: v for k, v in ngrams.items() if v > 1}
    if len(ngrams) == 0:
        print("No NGRAMS")
        pass
    else:
        ngrams = pd.DataFrame(list(ngrams.items()), columns=['combinations', 'count'])
        ngrams = ngrams.sort_values('count')
        #print(ngrams)
        
        plt.figure(2)
        sns.barplot("combinations", "count", data=ngrams).set_title(user)
        locs, labels = plt.xticks()
        plt.setp(labels, rotation=90)
        plt.savefig("plots/UID:%s_ngrams_%s.png" % (user, n))

#-------------------- type

if "anter" in string:
    print("type known: anterior")
if "immed" in string:
    print("type known: immediate")
if "poster" in string:
    print("type known: posterior")
if "panuv" in string:
    print("type known: panuveitis")
    