#!/usr/bin/env python

f = open("testfile","w")
f.write("This is our first test file")
f.close()

f = open("myfile","a")
f.write("Testing append mode")
f.close()

