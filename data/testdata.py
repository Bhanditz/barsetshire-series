import random, json, io

dum=[
    {   'topic': 'TOPIC1',
        'books': [
            {'b': []},
            {'b':[]},
            {'b':[]}
            ],
    },
    { 'topic': 'TOPIC2',
      'books': [
            {'b': []},
            {'b':[]},
            {'b':[]}
            ]
    },
    {   'topic': 'TOPIC3',
        'books': [
            {'b': []},
            {'b':[]},
            {'b':[]}
            ],
    },
    {   'topic': 'TOPIC4',
        'books': [
            {'b': []},
            {'b':[]},
            {'b':[]}
            ]
    },

]

def chapAdd(item,name, num, bchap):
    new={'chap':num+1, 'val': random.random(), 'len':10, 'nochap':bchap}
    item['b'].append(new)


b1chap=4
b2chap=7
b3chap=5

for elmt in dum:
    #for item in elmt['books']:
    for i in range(b1chap):
        chapAdd(elmt['books'][0], 'b1', i, b1chap)
    for j in range(b2chap):
        chapAdd(elmt['books'][1], 'b2', j, b2chap)
    for k in range(b3chap):
        chapAdd(elmt['books'][2], 'b3', k, b3chap)

with open('test.json','w') as f:
    dumdata= json.dumps(dum)
    f.write(dumdata)








