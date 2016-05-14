# -*- coding: UTF-8 -*-

# A grab bag of scripts and ideas of possible use for basic text mining
# using NLTK

from sys import argv
import os, re, nltk, json


    # with open(path_in) as file:
    # text = file.read()

    # # tokenize / break string into meaningful units, in this case words

    # tokens = nltk.word_tokenize(text)

    # # this separates out punctuation
    # tokens = nltk.WordPunctTokenizer().tokenize(s)

    # # this pattern strips punctuation
    # tokens = nltk.regexp_tokenizer(text, pattern=r'\w+')

    # # probably useful helper functions from os library
    # # for parsing files/folders

    # os.listdir():
    # os.mkdir()
    # os.getcwd()

    # # frequency distributions

    # fdist1 = nltk.FreqDist(tokens)
    # top_used = fdist1.most_common(500)
    # json.dumps()

def get_most_common_novels(path_in,num):
# gets most common words from texts and writes out
# to json files, according to path_in and number
# of common words to extract

    for i in os.listdir(path_in):
        with open(path_in + '/' + i) as f:
            text = f.read()
            tokens = nltk.word_tokenize(text)
            fdist = nltk.FreqDist(tokens)
            most_used = fdist.most_common(int(num))
            path_out = str.split(i,'.')[0]
            path_out += '.json'
            out = open(path_out,'w')
            out.write(json.dumps(most_used))
            out.close()

def get_most_common_combined(path_in,num):
# gets most common words from combining texts and writes out
# to json files, according to path_in and number of most
# common words to extract

    fulltext = ""
    for i in os.listdir(path_in):
      with open(path_in + '/' + i) as f:
        curr_vol = f.read()
        fulltext += " " + curr_vol
    tokens = nltk.word_tokenize(fulltext)
    fdist = nltk.FreqDist(tokens)
    most_used = fdist.most_common(int(num))
    out = open('combined-tokens.json','w')
    out.write(json.dumps(most_used))
    out.close()

if __name__ == '__main__':

    # takes two arguments, the filename and the number of most common
    # words
    # get_most_common_combined(argv[1],argv[2])
    get_most_common_novels("..\fulltext\Trollope_Warden_Text.txt",500)