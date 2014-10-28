'''
split a file into two randomly, line by line. 
Usage: small_split.py <input file> <output file 1> <output file 2> [<limit>] [<probability of writing to the first file>] [<random seed>]'
Example: python small_split.py source/twitter_corpus.csv source/twitter_train_small.csv source/twitter_test_small.csv 100 .8
'''

import csv
import sys
import random

input_file = sys.argv[1]
output_file1 = sys.argv[2]
output_file2 = sys.argv[3]

try:
	limit = int( sys.argv[4] )
except IndexError:
	limit = 1000

try:
	P = float( sys.argv[5] )
except IndexError:
	P = 0.9
	
try:
	seed = sys.argv[6]
except IndexError:
	seed = None
	
print "P = %s" % ( P )

if seed:
	random.seed( seed )



# calculate prob a row is included
i = open( input_file, 'r' )
reader = csv.reader( i )
row_count = sum(1 for r in reader)
prob = limit / float(row_count)

# reopen file after counting rows
i = open( input_file, 'r' )
o1 = open( output_file1, 'wb' )
o2 = open( output_file2, 'wb' )

reader = csv.reader( i )
writer1 = csv.writer( o1 )
writer2 = csv.writer( o2 )

for t, line in enumerate(reader):

	# randomly choose to include row
	r = random.random()
	if r > prob:
		continue
	
	# randomly allocate to train / test
	r = random.random()
	if r > P:
		writer2.writerow( line )
	else:
		writer1.writerow( line )
	"""
	if t >= limit:
		break
	if t <=1000000:
		writer1.writerow( line )
	else:
		writer2.writerow( line )

	if t % 100000 == 0:
		print t
	"""