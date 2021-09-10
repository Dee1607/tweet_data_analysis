# -*- coding: utf-8 -*-
#Drive mounting
from google.colab import drive
drive.mount('/content/drive')

import re
import os
import pandas as pd

import collections
import numpy as np
import math

def word_count(documents_words):
    documents_words = np.array(documents_words)
    # getting the elements frequencies using Counter class
    elements_count = collections.Counter(documents_words)
    return elements_count

tweets = []
documents_words = []
wordPerdocument = []
words = []
totalWords = []
path = '/content/drive/MyDrive/Data/Tweets/'
filenamesList = os.listdir('/content/drive/MyDrive/Data/Tweets/')
for filename in filenamesList:
  filepath = path + filename
  with open(filepath, encoding='utf-8') as filepath:
    dataframe = pd.read_csv(filepath)
    i = 0
    for text in dataframe['text'].to_list():
      i = i + 1
      documents_words,wordPerdocument,lengthTotalWords = SemanticAnalysis(text, i)
      elements_count = word_count(documents_words)
      words.append(len(wordPerdocument))
      totalWords.append(lengthTotalWords)
    
print(f"Query word : Document containing term(df) : Total Documents(N)/ number of documents term appeared(df) : Log10(N/df)")
for key, value in elements_count.items():
  Ndf= 500/value;
  log = math.log(500,value)
  print(f"{key}: {value} : {Ndf} : {log}")

print(" ")
print(f"documentNo : Total Words(m): frequency(f)")
for value in range(0,244):
  print(f"{value} : {totalWords[value]} : {words[value]}")

documents_words = []
wordPerdocument = []
def SemanticAnalysis(tweet, i):
    searchWords = ["flu", "snow", "cold"] 
    tweets = tweet.split()  
    count = 0
    for t in tweets:
      if t in searchWords:
        if count == 0:
          documents_words.append(t)
          count = 1
        if t == "flu":
          wordPerdocument.append(t)
    return documents_words, wordPerdocument, len(tweets)
