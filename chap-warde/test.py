'''
Just a place to test out code

'''
import os, re, json

corpus=set(["he","her","his","hers","him","himself","herself","she"])

path_in="chap-titles.json"

titles=[
	"Hiram's Hospital",
    "The Barchester Reformer",
    "The Bishop of Barchester",
    "Hiram's Bedesmen",
    "Dr Grantly Visits the Hospital",
    "The Warden's Tea Party",
    "_The Jupiter_",
    "Plumstead Episcopi",
    "The Conference",
    "Tribulation",
    "Iphigenia",
    "Mr Bold's Visit to Plumstead",
    "The Warden's Decision",
    "Mount Olympus",
    "Tom Towers, Dr Anticant, and Mr Sentiment",
    "A Long Day in London",
    "Sir Abraham Haphazard",
    "The Warden Is Very Obstinate",
    "The Warden Resigns",
    "Farewell",
    "Conclusion"
]

with open(path_in, "r") as infile:
	text=json.load(infile)
for line in text['warde']:
    print line


