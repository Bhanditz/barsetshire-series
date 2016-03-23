import json, os

#combined-tokens.json
#Trollope_Warden_text.json
#Trollope_Barchester_Towers_text.json

with open("Trollope_Barchester_Towers_text.json","r") as f:
    text = json.load(f)
    for line in text:
        print line[0]

