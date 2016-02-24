import random, json, io

b1chap=27
b2chap=60
b3chap=84
b4chap=48
b5chap=47
b6chap=53

dum=[
    {   'topic': 'TOPIC1',
        'books': [
            {'totalchap': b1chap, 'b':[]},
            {'totalchap': b2chap, 'b':[]},
            {'totalchap': b3chap, 'b':[]},
            {'totalchap': b4chap, 'b':[]},
            {'totalchap': b5chap, 'b':[]},
            {'totalchap': b6chap, 'b':[]}
            ]
    },
    { 'topic': 'TOPIC2',
      'books': [
            {'totalchap': b1chap, 'b':[]},
            {'totalchap': b2chap, 'b':[]},
            {'totalchap': b3chap, 'b':[]},
            {'totalchap': b4chap, 'b':[]},
            {'totalchap': b5chap, 'b':[]},
            {'totalchap': b6chap, 'b':[]}
            ]
    },
    {   'topic': 'TOPIC3',
        'books': [
            {'totalchap': b1chap, 'b':[]},
            {'totalchap': b2chap, 'b':[]},
            {'totalchap': b3chap, 'b':[]},
            {'totalchap': b4chap, 'b':[]},
            {'totalchap': b5chap, 'b':[]},
            {'totalchap': b6chap, 'b':[]}
            ]
    },
    {   'topic': 'TOPIC4',
            'books': [
            {'totalchap': b1chap, 'b':[]},
            {'totalchap': b2chap, 'b':[]},
            {'totalchap': b3chap, 'b':[]},
            {'totalchap': b4chap, 'b':[]},
            {'totalchap': b5chap, 'b':[]},
            {'totalchap': b6chap, 'b':[]}
            ]
    },

]

def chapAdd(item, name, num):
    new={'chap':num+1, 'val': random.random()}
    item['b'].append(new)


for elmt in dum:
    for i in range(b1chap):
        chapAdd(elmt['books'][0], 'b1', i)
    for j in range(b2chap):
        chapAdd(elmt['books'][1], 'b2', j)
    for k in range(b3chap):
        chapAdd(elmt['books'][2], 'b3', k)
    for l in range(b4chap):
        chapAdd(elmt['books'][3], 'b4', l)
    for m in range(b5chap):
        chapAdd(elmt['books'][4], 'b5', m)
    for n in range(b6chap):
        chapAdd(elmt['books'][5], 'b6', n)

with open('test.json','w') as f:
    dumdata= json.dumps(dum)
    f.write(dumdata)

