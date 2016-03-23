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
	"gender": [#"he","her","his","hers","him","himself","herself","she",
		"Mr","Mrs","Ms","man","woman","men","women","father","mother",
		"son","daughter","brother","sister","sir","love","papa",
		"mamma","gentleman","lady","wife","husband","children","family",
		"girl","boy","marry","married","marriage","child"
		],
	"class": ['archdeacon', 'bishop', 'dr', 'friend', 'old', 'wife', 
		'church', 'poor', 'income', 'doctor', 'woman', 'men', 'money', 'dean', 'lord', 'squire', 'family', 'lady', 'public', 'pounds', 'husband', 'rate', 'brother', 'clergyman', 'precentor', 'st', 'alone', 'declared', 'duty', 'palace', 'london', 'power', 'girl', 'carriage', 'gentleman', 'widow', 'lordship', 'children', 'ladies', 'married', 'attorney-general', 'appointment', 'opinion', 'lawyer', 'property', 'business', 'justice', 'service', 'oxford', 'pay', 'england', 'rich', 'bedesmen', 'wardenship'
		],
	"abstract": ['know', 'think', 'never', 'thought', 'nothing', 'time',
		'love', 'mind', 'world', 'year', 'heart', 'always', 'moment', 'life', 'money', 'present', 'place', 'name', 'soon', 'poor', 'wish', 'public', 'home', 'till', 'doubt', 'hope', 'happy', 'together', 'things', 'anything', 'morning', 'best', 'understand', 'idea', 'truth', 'while', 'known', 'quiet', 'duty', 'comfort', 'power', 'hour', 'thinking', 'feeling', 'days', 'age', 'evening', 'impossible', 'live', 'opinion', 'care', 'possible', 'hard', 'law', 'tone', 'order', 'conduct', 'occasion', 'circumstances', 'fact', 'loved', 'feelings', 'nature', 'evil', 'justice', 'character', 'strong', 'charity', 'believe', 'promise', 'angry', 'rich', 'sorrow'
		],
	"conflict": ['no', "n't", 'can', 'say', 'never', 'though', 'other', 'thought', 'nothing', 'too',
		'without', 'only', 'however', 'also', 'felt', 'ever', 'What', 'new', 'yet', 'against', 'another', 'nor', 'why', 'question', 'enough', 'better', 'wrong', 'thus', 'whether', 'certainly', 'understand', 'idea', 'petition', 'truth', 'answer', 'declared', 'power', 'angry', 'Bold', 'ask', 'gone', 'end', 'continued', 'known', 'know', 'bear', 'impossible', 'duty', 'knows', 'opinion', 'care', 'possible', 'lawyer', 'law', 'probably', 'nearly', 'order', 'conduct', 'feelings', 'advice', 'allow', 'evil', 'justice', 'angry', 'duties', 'fear'
		]
	}