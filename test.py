
"""
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pprint
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
print negids[0] 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
pprint.pprint(negfeats[0])
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
"""


import pprint
import csv
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

train = 'source/twitter_train_small.csv'
reader = csv.reader( open( train, 'r' ))#, delimiter = '\t' )
negfeats = []
posfeats= []
for t, r in enumerate(reader):
	
	if t%100000 == 0 and t > 0:
		print "parsing row: %s" % (t)
	
	# select data source
	if len(r) == 6:
		pprint.pprint(r)
		sentiment = r[0]
		text = r[5]
	elif len(r) == 4:
		sentiment = r[1]
		text = r[3]
	else:
		continue

	
	text = text.lower()
	# split text string into chunks and remove trailing punctuation
	text_split = [i[:-1] if i[-1] in ['.', ',', '?', '!'] else i for i in text.split()]
	feats = word_feats(text_split)
	if int(sentiment) == 0:
		negfeats.append( (feats, 'neg') )
	else:
		posfeats.append( (feats, 'pos') )

negcutoff = len(negfeats)*4/5
poscutoff = len(posfeats)*4/5

print "combining train and test sets"
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
"""
st = "&lt;3 Beatles Rockband, watching today's E3 recorded? from G4 "
st = st.lower()
print st
print st.split()
print [i[:-1] if i[-1] in ['.', ',', '?', '!'] else i for i in st.split()]
print "".join((char if char.isalpha() else " ") for char in st).split()
"""