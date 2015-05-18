#!/usr/bin/python

#easy for extract info from json

import json
from sys import argv

if __name__ ==  "__main__":
	#original json file
	f = open(argv[1], 'r')
	j = json.load(f)
	#target file
	f2 = open(argv[2], 'w')
	f2.write(j['msg'][1].encode('utf-8'))
	f.close()
	f2.close()
