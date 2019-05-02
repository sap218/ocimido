#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:35:20 2019
@author: samantha

TYPE of Uveitis of users
"""

from collections import Counter
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import json

#-------------------- importing JSON
def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))
posts = js_r('output.json')

#-------------------- getting list of all users
users = []
for post in posts:
    for comment in post:
        if "user_link" in comment:
            users.append(comment["user_link"])

users = [x for x in users if x is not None]
uids = dict(Counter(users))
uids = list(uids)

#-------------------- getting list of comments for particular user
anterior = 0
immediate = 0
posterior = 0
panuveitis = 0

for item in uids:
    comments = []
    for post in posts:
        for comment in post:
            if item in comment.values():
                if "post_text" in comment:
                    comments.append(comment["post_text"])

    comments = [item for sublist in comments for item in sublist]
    comments = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in comments] # removing special characters
    comments = ''.join(comments) # joining 
    comments = comments.lower()

    #-------------------- nltk
    stopWords = set(stopwords.words('english'))
    comments = word_tokenize(comments)
    wordsFiltered = [] # removing stop words
    for item in comments:
        if item not in stopWords:
            wordsFiltered.append(item)
    stemming = [] 
    ps = PorterStemmer()
    for item in wordsFiltered:
        stemming.append(ps.stem(item))
    string = stemming 
    string = ' '.join(map(str, string)) 
    
    #-------------------- type
    
    if "anter" in string:
        anterior += 1
    if "immed" in string:
        immediate += 1
    if "poster" in string:
        posterior += 1
    if "panuv" in string:
        panuveitis += 1
    
#-------------------- counting
all_count = len(uids)
print("Total\tUSERS\t\t%s" % (all_count))
print("Total\tANTERIOR\t%s\t\t16.585365853658537" % (anterior))
print("Total\tIMMEDIATE\t%s\t\t9.268292682926829" % (immediate))
print("Total\tPOSTERIOR\t%s\t\t10.24390243902439" % (posterior))
print("Total\tPANUVEITIS\t%s\t\t5.365853658536586" % (panuveitis))

count = anterior + immediate + posterior + panuveitis
print("Total\tUNKNOWN\t\t%s\t\t58.536585365853654" % (all_count-count))