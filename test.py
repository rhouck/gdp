import pprint
"""
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

import sys
import string
import simplejson
from twython import Twython, TwythonError

import datetime
from dateutil.parser import parse
now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)


t = Twython(app_key='SodtZPLaiPy85X9HQhXZ6l9bv', 
    app_secret='RMuNAx9Iam8zRx5gjoGUO29uzOL06zZy79xvyaUaYn60Kd9ZF6',
    oauth_token='2881134812-1mhCU7r0rSWX8JFghBARThAOM5LyPRJg1EZhdYS',
    oauth_token_secret='ibEDSNodxKo8c5nPrblwet676yn7nUKboSCQlArhvEvB2')

"""
ids = "4816,9715012,13023422, 13393052,  14226882,  14235041, 14292458, 14335586, 14730894,"
    
users = t.lookup_user(user_id = ids)

fields = "id screen_name name created_at url followers_count friends_count statuses_count \
    favourites_count listed_count \
    contributors_enabled description protected location lang expanded_url".split()

outfn = "source/twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year) 
outfp = open(outfn, "w")
outfp.write(string.join(fields, "\t") + "\n")  # header

for entry in users:
    #CREATE EMPTY DICTIONARY
    r = {}
    for f in fields:
        r[f] = ""
    #ASSIGN VALUE OF 'ID' FIELD IN JSON TO 'ID' FIELD IN OUR DICTIONARY
    r['id'] = entry['id']
    #SAME WITH 'SCREEN_NAME' HERE, AND FOR REST OF THE VARIABLES
    r['screen_name'] = entry['screen_name']
    r['name'] = entry['name']
    r['created_at'] = entry['created_at']
    r['url'] = entry['url']
    r['followers_count'] = entry['followers_count']
    r['friends_count'] = entry['friends_count']
    r['statuses_count'] = entry['statuses_count']
    r['favourites_count'] = entry['favourites_count']
    r['listed_count'] = entry['listed_count']
    r['contributors_enabled'] = entry['contributors_enabled']
    r['description'] = entry['description']
    r['protected'] = entry['protected']
    r['location'] = entry['location']
    r['lang'] = entry['lang']
    #NOT EVERY ID WILL HAVE A 'URL' KEY, SO CHECK FOR ITS EXISTENCE WITH IF CLAUSE
    if 'url' in entry['entities']:
        r['expanded_url'] = entry['entities']['url']['urls'][0]['expanded_url']
    else:
        r['expanded_url'] = ''
   
    #CREATE EMPTY LIST
    lst = []
    #ADD DATA FOR EACH VARIABLE
    for f in fields:
        lst.append(unicode(r[f]).replace("\/", "/"))
    #WRITE ROW WITH DATA IN LIST
    outfp.write(string.join(lst, "\t").encode("utf-8") + "\n")
 
outfp.close()
"""
"""
search_results = t.search(q="@united", count=5)
try:
    for tweet in search_results["statuses"]:
        created = parse(tweet['created_at'])
        # ignore retweeted content
        #if tweet['text'][:2] == "RT":
        #	continue
        print created
        print tweet['text']
except TwythonError as e:
    print e
"""

from alchemyapi_python.alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#myText = "I'm excited to get started with AlchemyAPI!"
#response = alchemyapi.sentiment("text", myText)
#print "Sentiment: ", response["docSentiment"]["type"]

articles = [
    ["October 24, 2014, Friday", "http://www.nytimes.com/2014/10/24/business/cheaper-fuel-helps-airlines-to-record-profits.html"],
    ["26-Sep-14", "http://www.ft.com/cms/s/0/05aa74a4-457f-11e4-ab86-00144feabdc0.html"]
]
sentiments = []
for a in articles:
    try:
        response = alchemyapi.sentiment("url", a[1])
        result = {'date': parse(a[0]), 
                'sentiment-type': response["docSentiment"]["type"], 
                'sentiment-score': response["docSentiment"]["score"],
                'sentiment-mixed': response["docSentiment"]["mixed"]
                }
        sentiments.append(result)
    except:
        pass

pprint.pprint(sentiments)




