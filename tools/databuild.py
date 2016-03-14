import os, re, nltk, json, sklearn

#lengths of warde, barch, docto, framl, smallh, lastc
chapter_lengths = [21,53,47,48,60,84]
books = ["warde", "barch", "docto", "framl","smallh","lastc"]
book_titles=["Warden", "Barchester_Towers","Doctor_Thorne",
	"Framley_Parsonage","Small_House", "Last_Chronicle"]
	
chapter_titles = []


master_dict = []


corpus0 = ["he","her","his","hers","him","himself","herself","she",
	"Mr","Mrs","Ms","man","woman","men","women","father","mother",
	"son","daughter","brother","sister","Sir","sir","love","papa",
	"mamma","gentleman","lady","wife","husband","children","family",
	"girl","boy","marry","married","marriage","child"
]


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
	
def makeTitles(path_in, name):
	#Makes list of chapter titles
	new=[]
	with open(path_in, "r") as infile:
		titles = json.load(infile)
	for line in titles[name]:
		new.append(line)
	chapter_titles.append(new)
	
	
def freqMetric(tok,corp):
	#General frequency metric. 
	#This counts number of hits,
	# but can be more complex
	tok_set = set(tok)
	corp_set = set(corp)
	inter = tok_set.intersection(corp_set)
	return len(inter)/float(len(corp))
	
def numZero(num):
	#Determines if end of file ends as
	# 00x or 0xx
	if len(str(num)) == 1:
		return "00"+str(num)
	else:
		return "0"+str(num)
		
def readChap(path_in, corp):
	#Reads in the chapter, returns a 
	# value to measure frequency 
	with open(path_in, "r") as infile:
		text = infile.read().decode("utf-8")
		tokens = nltk.word_tokenize(text)
		return freqMetric(tokens,corp)

	
def genData(tpc):
	addTopic(tpc)
	#goes through each book, sets up paths
	for b in range(len(books)):
		path0 = "../chap-" + books[b]
		book_path = path0 +"/Trollope_" + book_titles[b] + "_text_"
		print book_path
		makeTitles(path0+"/chap-titles.json", books[b])
		addInfo(book_titles[b],chapter_lengths[b],master_dict[0]['books'])
		#runs through each chapter
		for c in range(chapter_lengths[b]):
			chap_path = book_path + numZero(c+1)+".txt"
			value = readChap(chap_path,corpus0)
			name = chapter_titles[b][c]
			addChap(name,value,master_dict[0]['books'][b]['b'])
		
genData("gender")

with open("../vis-data/data.json","w") as outfile:
	dum = json.dumps(master_dict)
	outfile.write(dum)