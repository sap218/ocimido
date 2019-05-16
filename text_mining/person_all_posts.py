#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:09:52 2019
@author: samantha

ALL posts of an individual user
"""

#-------------------- packages

import json
import re
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#fig_size = plt.rcParams["figure.figsize"]
#fig_size[0] = 30
#fig_size[1] = 15
#plt.rcParams["figure.figsize"] = fig_size

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams

#-------------------- functions
def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))
       
def get_all_id(posts):
    uids = []
    for post in posts:
        for comment in post:
            if "user_link" in comment:
                uids.append(comment["user_link"])
    return uids
def uids_post_count(uids):
    count = dict(Counter(uids))
    return count

def get_all_comments(posts, uid):
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
    return comments

def nltk(string):
    stopWords = set(stopwords.words('english'))
    string = word_tokenize(string)
    wordsFiltered = [] # removing stop words
    for item in string:
        if item not in stopWords:
            wordsFiltered.append(item)
    stemming = [] 
    ps = PorterStemmer()
    for item in wordsFiltered:
        stemming.append(ps.stem(item))
    stemming = ' '.join(stemming)
    return stemming

def ngramming(string):
    bigramming = ngrams(string.split(), 2)
    trigramming = ngrams(string.split(), 3)
    bigrams = []
    for item in bigramming:
        bigrams.append(item)
    trigrams = []
    for item in trigramming:
        trigrams.append(item)
    return bigrams, trigrams

def type_of_uv(user_post):
    anterior = comments.count("anterior")
    intermedi = comments.count("intermedi")
    posterior = comments.count("posterior")
    panuv = comments.count("panuv")
    type_of = (str(anterior) + str(intermedi) + str(posterior) + str(panuv))
    return type_of

def getting_popular(comments):
    bigrams, trigrams = ngramming(comments)
    popular_bigrams = dict(Counter(bigrams))
    popular_trigrams = dict(Counter(trigrams))
    
    comments = comments.split()
    popular_words = dict(Counter(comments))
    
    return popular_words, popular_bigrams, popular_trigrams

#-------------------- code

if __name__ == "__main__": 
    posts = js_r('output.json')  
    
    uids = get_all_id(posts)
    uid_post_count = uids_post_count(uids) # getting user comments count
    
    uids = list(set(uids))
    uids = [x for x in uids if x is not None] # removing NULL uid
    
    list_uid = []
    list_comments = []
    list_types = []
    list_bigrams = []
    list_trigrams = []
    
    for uid in uids:
        #uid = uids[55] # using this UID | 55 & 34
        comments = get_all_comments(posts, uid) # users' all comments
    
        comments = nltk(comments) # NLTK
    
        #popular_words, popular_bigrams, popular_trigrams = getting_popular(comments)
        type_of = type_of_uv(comments)
    
        list_uid.append(uid)
        list_comments.append(comments)
        list_types.append(type_of)

        bigrams, trigrams = ngramming(comments)
        list_bigrams.append(bigrams)
        list_trigrams.append(trigrams)
    

    '''
    stemming = pd.DataFrame(list(stemming.items()), columns=['words', 'count'])
    stemming = stemming.sort_values('count')    
    plt.figure(1)
    sns.barplot("words", "count", data=stemming).set_title(user)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.savefig("plots/UID:%s_top-words.png" % (user))    
    '''
