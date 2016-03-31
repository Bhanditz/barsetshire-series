import os, re, nltk, json, sklearn
from freqmetrics import *

#lengths of warde, barch, docto, framl, smallh, lastc
chapter_lengths = [21,53,47,48,60,84]
books = ["warde", "barch", "docto", "framl","smallh","lastc"]

book_titles=["Warden", "Barchester_Towers","Doctor_Thorne",
	"Framley_Parsonage","Small_House", "Last_Chronicle"]
	
chapter_titles = {}

master_dict = []


def addTopic(tpc):
	#Adds a new topic to the json array
	newtpc = {'topic': tpc, 'books':[]}
	master_dict.append(newtpc)
	
def addInfo(title, no_chaps,book):
	#Adds title of book and number
	# of chapters to the json
	newbook = {'title': title, 'totalchap':no_chaps, 'b':[]}
	book.append(newbook)
	
def addChap(title, value, book):
	#Adds a new chapter title and value
	# to each book
	new = {'chap': title, 'val': value}
	book.append(new)
	
def makeTitles(path_in, name, realtitle):
	#Makes list of chapter titles
	# puts them into a dictionary
	index=1
	chapter_titles[name]={}
	chapter_titles[name]["chapters"]={}
	chapter_titles[name]["trunc"]=name
	chapter_titles[name]["realtitle"]=realtitle
	with open(path_in, "r") as infile:
		titles = json.load(infile)
	for line in titles[name]:
		chapter_titles[name]["chapters"][line] = {}
		chapter_titles[name]["chapters"][line]["index"] = index
		index = index +1
	
	
def numZero(num):
	#Determines if end of file ends as
	# 00x or 0xx
	if len(str(num)) == 1:
		return "00"+str(num)
	else:
		return "0"+str(num)
		
def readChap(path_in, title, chap):
	#Reads in the chapter, puts 
	# list of tokens in main dictionary
	with open(path_in, "r") as infile:
		text = infile.read().decode("utf-8")
		tokens = nltk.word_tokenize(text)
		#MAKE LOWER CASE
		#tokens = tokenize[w.lower() for w in tokenize]
		#return corpFreq(tokens,corp)
		chapter_titles[title]["chapters"][chap]["tokens"]=tokens

def makeBookLists():
	for b in range(len(books)):	
		path0 = "../chap-" + books[b]
		book_path = path0 +"/Trollope_" + book_titles[b] + "_text_"
		print book_path
		makeTitles(path0+"/chap-titles.json", books[b], book_titles[b])
	#	for c in range(chapter_lengths[b]):
	#		chap_path = book_path + numZero(c+1)+".txt"
	#		readChap(chap_path,books[b])
	for title in chapter_titles:
		path0 = "../chap-" + chapter_titles[title]["trunc"]
		book_path = path0 + "/Trollope_" + chapter_titles[title]["realtitle"] + "_text_"
		for c in chapter_titles[title]["chapters"]:
			num = chapter_titles[title]["chapters"][c]["index"]
			chap_path = book_path + numZero(num) + ".txt"
			readChap(chap_path, title, c)
			

def genData(topic,j):
	addTopic(topic)
	#for title in chapter_titles:
	for k in range(len(books)):
		for titlesrch in chapter_titles:
			if chapter_titles[titlesrch]['trunc'] == books[k]:
				title = titlesrch
		bookname = chapter_titles[title]['realtitle']
		num = len(chapter_titles[title]['chapters'])
		addInfo(bookname,num, master_dict[j]['books'])
		for i in range(num):
			ind = i+1
			#search for index 
			for dum in chapter_titles[title]['chapters']:
				if chapter_titles[title]['chapters'][dum]['index'] == ind:
					#print chapter_titles[title]['chapters'][dum]['index']
					chaptertok = dum
			#search for index in master_dict
			mast_index=0
			for srch in master_dict[j]['books']:
				if srch['title'] == bookname:
					break
				else:
					mast_index=mast_index+1
			#print mast_index	
			toklst = chapter_titles[title]['chapters'][chaptertok]['tokens']
			value = chapFreq(toklst, allcorps[topic])
				
			addChap(chaptertok, value, master_dict[j]['books'][mast_index]['b'])
			
	
		
makeBookLists()
for i in range(len(allcorps)):			
	genData(allcorps.keys()[i],i)


#print master_dict

#for i in master_dict[0]['books'][0]['b']:
#	print i


with open("../vis-data/data.json","w") as outfile:
	dummy = json.dumps(master_dict)
	outfile.write(dummy)
