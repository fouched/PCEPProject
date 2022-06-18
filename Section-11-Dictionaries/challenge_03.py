
sentence = 'I am so happy to learn Python which makes my wife happy and interested in Python Python Python Python'
occurs = {}

for x in sentence.split():
    occurs[x] = sentence.count(x)

print(f'Word count {occurs}')
