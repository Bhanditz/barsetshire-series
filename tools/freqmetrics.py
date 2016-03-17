def corpFreq(tok,corp):
	#Only counts each corpus word that
	# appear in the chapter. Does not
	# count them more than once.
	#Returns total hits divided by 
	# length of corpus.
	tok_set = set(tok)
	corp_set = set(corp)
	inter = tok_set.intersection(corp_set)
	return len(inter)/float(len(corp))
	
def chapFreq(tok,corp):
	#Counts frequency of corpus words
	# that appear in the chapter.
	#Returns total freq divided by
	# chapter length.
	counts = {}
	total = 0
	for word in tok:
		if word in counts:
			counts[word] = counts[word] + 1
		else:
			counts[word] = 1
	for elmt in counts:
		if elmt in corp:
			total = total + counts[elmt]
	return float(total)/len(tok)
		