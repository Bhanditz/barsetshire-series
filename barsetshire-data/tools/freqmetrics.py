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
		
		
allcorps = {
	"Gender": [#"he","her","his","hers","him","himself","herself","she",
		"Mr","Mrs","Ms","man","woman","men","women","father","mother",
		"son","daughter","brother","sister","sir","love","papa",
		"mamma","gentleman","lady","wife","husband","children","family",
		"girl","boy","marry","married","marriage","child"
		],
	"Class": ['archdeacon', 'bishop', 'dr', 'friend', 'old', 'wife', 
		'church', 'poor', 'income', 'doctor', 'woman', 'men', 'money', 'dean', 'lord', 'squire', 'family', 'lady', 'public', 'pounds', 'husband', 'rate', 'brother', 'clergyman', 'precentor', 'st', 'alone', 'declared', 'duty', 'palace', 'london', 'power', 'girl', 'carriage', 'gentleman', 'widow', 'lordship', 'children', 'ladies', 'married', 'attorney-general', 'appointment', 'opinion', 'lawyer', 'property', 'business', 'justice', 'service', 'oxford', 'pay', 'england', 'rich', 'bedesmen', 'wardenship'
		],
	"Writing": ['letter', 'write', 'read', 'written', 'letters', 'note', 'wrote', 'writing', 'received', 'table', 'paper', 'send', 'answer', 'return', 'handed', 'desk', 'pen', 'addressed', 'think', 'tell', 'word', 'thinking', 'thought', 'words', 'To', 'receive'
	],
	"Concepts": ['nothing', 'love', 'world', 'heart', 'life', 'money', 'place', 'poor', 'wish', 'home', 'doubt', 'hope', 'happy', 'together', 'things', 'best', 'idea', 'truth', 'quiet', 'duty', 'comfort', 'power', 'impossible', 'live', 'possible', 'law', 'order', 'conduct', 'occasion', 'circumstances', 'fact', 'loved', 'feelings', 'nature', 'evil', 'justice', 'character', 'strong', 'charity', 'believe', 'promise', 'angry', 'rich', 'sorrow'
	],
	"Talking": ['can', 'say', 'though', 'other', 'thought', 'without', 'only', 'also', 'felt', 'why', 'question', 'whether', 'understand', 'idea', 'truth', 'answer', 'declared', 'power', 'angry', 'Bold', 'ask', 'known', 'know', 'bear', 'duty', 'knows', 'opinion', 'care', 'possible', 'lawyer', 'law', 'probably', 'nearly', 'order', 'conduct', 'feelings', 'advice', 'allow', 'justice', 'duties'
	],
	"Domestic": ['Mr', 'man', 'Mrs', 'himself', 'Lady',
		'father', 'Miss', 'Sir', 'herself', 'friend', 'house', 'love', 'wife', 'Mr', 'man', 'Mrs', 'himself', 'Lady', 'father', 'Miss', 'Sir', 'herself', 'friend', 'house', 'love', 'wife', 'Mr', 'Mr', 'man', 'Mrs', 'himself', 'Lady', 'father', 'Miss', 'Sir', 'herself', 'friend', 'house', 'love', 'wife', 'Mr', 'house', 'room', 'poor', 'husband', 'son-in-law', 'home', 'family', 'quiet', 'comfort', 'palace', 'party', 'carriage', 'door', 'brother', 'wife', 'mamma', 'table', 'sister', 'mother', 'dinner', 'garden', 'daily'
	]
	}