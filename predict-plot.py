#This code reads one text file at a time

from nltk import word_tokenize, pos_tag, ne_chunk

# read a text file
text = file ('/home/foo/Desktop/iDevji/nltk-NER/sherlock/fina.txt')

# replace \n with a spcae
data=text.read().replace('\n', ' ')

chunked =  ne_chunk (pos_tag ( word_tokenize (data) ))

# extract GPEs
extracted = []
for chunk in chunked:
	if hasattr (chunk, 'label'):
		if chunk.label() == 'GPE':
			extracted.append (''.join (c[0] for c in chunk))

# extract most frequent GPE

from collections import Counter
count = Counter(extracted)
count.most_common(1)
