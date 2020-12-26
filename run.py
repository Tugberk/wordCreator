from itertools import chain, combinations, permutations
import re
import sys

#myword = 'myword'
myword = sys.argv[1]


def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def findif(mystr):	
	with open('kokler.txt') as search:
		for line in search:
			line = line.rstrip()
			if mystr == line:
				print 'found: ', line


for i in list(powerset(myword)):

	#print i
	for x in permutations(i):
		findif(''.join(x))


