#!/usr/bin/env python
import sys
def readfile(filename):
	f = open(filename,'rt') 
	#with open(filename,'rt') as f:
	for i in f:
		#i = i.strip() 
#we use strip() to remove all the leading and trailing spaces from a string
		#print(i)
# ----------------------------------
#we can also use the write method of standard out stream to print our file without adding extra spaces.
		sys.stdout.write(i)
	f.close() #Closing the file after use is very important. We can use "with-block" to close the file automatically without calling the close()

if __name__ == '__main__':
	readfile(sys.argv[1])



