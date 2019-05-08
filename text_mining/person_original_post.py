#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:09:52 2019
@author: samantha

ORIGINAL post of user
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

def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in)) # importing JSON
posts = js_r('/home/samantha/PhD_ontology/other_json/posts.json')

#-------------------- post check
print("Total count of posts\t1-%s" % (len(posts)))
query = input("What post do you wish to check?\t")
while int(query) > 416 or int(query) == 0:
    query = input("What post do you wish to check?\t")
query = int(query)-1    
post = posts[query]

#-------------------- users' post
try:
    user_link = [x["user_link"] for x in post]
    user_link = user_link[0]
    uid = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in user_link]
    uid = uid[-10:]
    uid = ''.join(uid)
    uid = uid.replace(" ", "")
except TypeError:
        uid = "ANON"

#-------------------- getting user posts
person_posts = list(filter(lambda person: person['user_link'] == user_link, post)) # getting persons' posts
person_posts = [" ".join(x["post_text"]) for x in person_posts] # joining text
person_posts = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in person_posts] # removing special characters
person_posts = ''.join(person_posts) # joining 

#-------------------- stop words
stopWords = set(stopwords.words('english'))
person_posts = word_tokenize(person_posts)
wordsFiltered = [] # removing stop words
for item in person_posts:
    if item not in stopWords:
        wordsFiltered.append(item)
del stopWords

#-------------------- shortening & plotting
stemming = [] 
ps = PorterStemmer()
for item in wordsFiltered:
    stemming.append(ps.stem(item))
string = stemming
stemming = dict(Counter(stemming))
stemming = {k: v for k, v in stemming.items()} # if v > 1
stemming = pd.DataFrame(list(stemming.items()), columns=['words', 'count'])
stemming = stemming.sort_values('count')

plt.figure(1)
sns.barplot("words", "count", data=stemming).set_title(uid)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.savefig("plots/P:%s_UID:%s_top-words.png" % ((query+1), uid))


#-------------------- NGRAMS
string = ' '.join(map(str, string)) 
n = int(input("NGRAM\t(2 / 3):\t\t"))
sixgrams = ngrams(string.split(), n)
ngrams = []
for item in sixgrams:
    ngrams.append(item)
ngrams = dict(Counter(ngrams))
norg = ngrams
ngrams = {k: v for k, v in ngrams.items() if v > 1}

if len(ngrams) < 2:
    print("\nNo major NGRAMS\n")
    pass
    #for item in norg:
    #    print(item)
else:
    ngrams = pd.DataFrame(list(ngrams.items()), columns=['combinations', 'count'])
    ngrams = ngrams.sort_values('count')
    plt.figure(2)
    sns.barplot("combinations", "count", data=ngrams).set_title(uid)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.savefig("plots/P:%s_UID:%s_ngrams_%s.png" % ((query+1), uid, n))
    

#-------------------- type

if "anteri" in string:
    print("type known: anterior")
if "intermedi" in string:
    print("type known: intermediate")
if "posteri" in string:
    print("type known: posterior")
if "panuveit" in string:
    print("type known: panuveitis")
    
