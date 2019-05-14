#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:56:11 2019
@author: samantha
"""

import json
import re
from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 30
fig_size[1] = 15
plt.rcParams["figure.figsize"] = fig_size
'''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams

#-------------------- functions

def json_get(filename):
   with open(filename) as f_in:
       return(json.load(f_in)) # importing JSON
    
def getting_uid(thread):
    user_link = thread[0].get('user_link')
    return user_link

def getting_user_posts_only(thread, user_link):
    if user_link is None:
        sentences = thread[0]['post_text']
        sentences = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in sentences]
        sentences = ''.join(sentences)
    else:
        sentences = list(filter(lambda person: person['user_link'] == user_link, thread)) # getting persons' posts
        sentences = [" ".join(x["post_text"]) for x in sentences] # joining text
        sentences = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in sentences] # removing special characters
        sentences = ' '.join(sentences) # joining 
        sentences = sentences.lower()
    return sentences

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

def type_of_uv(string):
    anterior = 0
    intermedi = 0
    posterior = 0
    panuv = 0
    if "anterior" in user_post:
        anterior += 1
    if "intermedi" in user_post:
        intermedi +=1
    if "posterior" in user_post:
        posterior += 1
    if "panuv" in user_post:
        panuv += 1
    type_of = (str(anterior) + str(intermedi) + str(posterior) + str(panuv))
    return type_of
    
#-------------------- code

if __name__ == "__main__":    
    posts = json_get('output.json')    
    
    df = pd.DataFrame()
    list_text = []
    list_uids = []
    list_type = []
        
    interesting_words = ["anterior", "intermedi", "posterior", "panuv"]
    for post in posts:
        #post = posts[p] # 13 ANON
        user_link = getting_uid(post)
        user_post = getting_user_posts_only(post, user_link) 
        user_post = nltk(user_post)
        user_post = ' '.join(user_post)
        
        list_text.append(user_post) # texts
        list_uids.append(user_link) # user_links
        list_type.append(type_of_uv(user_link)) # type of uveitis
    df = list(zip(list_text, list_uids, list_type))
    df = pd.DataFrame(df, columns = ['text' , 'uid', 'type']) 
    df.uid.replace([None], ("ANON"), inplace=True)
    #df['uid'].value_counts()
    list_strings = ' '.join(list_text)
    
    '''
    nonANONS = df
    nonANONS.uid.replace(["ANON"], ("0"), inplace=True)
    nonANONS = nonANONS[nonANONS['uid'] != "0"]
    newdf = nonANONS.groupby(['uid','type'])['text'].apply(', '.join).reset_index()
    newdf = newdf.groupby(['uid','type'])['text'].apply(', '.join).reset_index()
    '''
    
    
    #-------------------- type plot 
    types = []
    for item in df.type:
        types.append(item)
    types = dict(Counter(types))
    types = pd.DataFrame(list(types.items()), columns=['type', 'count'])
    types = types.sort_values('count', ascending=False)
    #plt.figure(1)
    #sns.barplot("type", "count", data=types).set_title("type")
    #locs, labels = plt.xticks()
    #plt.setp(labels, rotation=45)

    people_with = []
    people = (df.loc[df['type'] != '0000'])
    for item in people.uid:
        people_with.append(item)
    while "ANON" in people_with:
        people_with.remove("ANON")
    people_with = set(people_with)
    del people, item
    
    people_without = []
    people = (df.loc[df['type'] == '0000'])
    for item in people.uid:
        people_without.append(item)
    #while "ANON" in people_without:
    #    people_without.remove("ANON")
    people_without = set(people_without)
    del people, item
    
    #-------------------- grams
    bigrams, trigrams = ngramming(list_strings)
    popular_bigrams = dict(Counter(bigrams))
    popular_trigrams = dict(Counter(trigrams))
    del bigrams, trigrams    
    popular_bigrams = pd.DataFrame(list(popular_bigrams.items()), columns=['bigrams', 'count'])
    popular_bigrams = popular_bigrams.sort_values('count', ascending=False)
    popular_bigrams = popular_bigrams[popular_bigrams['count'] >= 20]
    popular_trigrams = pd.DataFrame(list(popular_trigrams.items()), columns=['trigrams', 'count'])
    popular_trigrams = popular_trigrams.sort_values('count', ascending=False)
    popular_trigrams = popular_trigrams[popular_trigrams['count'] >= 5]

    #-------------------- popular
    list_strings = list_strings.split()
    popular_words = dict(Counter(list_strings))
    
    popular = pd.DataFrame(list(popular_words.items()), columns=['words', 'count'])
    popular = popular.sort_values('count', ascending=False)
    popular = popular[popular['count'] >= 100]
    #plt.figure(2)
    #sns.barplot("words", "count", data=popular).set_title("user_link")
    #locs, labels = plt.xticks()
    #plt.setp(labels, rotation=45)
    
    
    '''
    df.type.replace(("1000", "0100", "0010", "0001",
                     "1100", "1010", "1001",
                     "0101","0110",
                     "0011",
                     "1110",
                     "1111"), 
                    (interesting_words[0],interesting_words[1],interesting_words[2],interesting_words[3],
                     interesting_words[0]+interesting_words[1],interesting_words[0]+interesting_words[2],interesting_words[0]+interesting_words[3],
                     interesting_words[1]+interesting_words[2],interesting_words[1]+interesting_words[3],
                     interesting_words[2]+interesting_words[3],
                     interesting_words[0]+interesting_words[1]+interesting_words[2],
                     interesting_words[0]+interesting_words[1]+interesting_words[2]+interesting_words[3]), 
                    inplace=True)
    df['type'].value_counts()    
    '''    