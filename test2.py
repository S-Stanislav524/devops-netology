#!/usr/bin/env python3
import os
import socket
from urllib2 import urlopen
with open("./test.txt", "r+w") as file_:
	NewStr = ""
	for item in file_:
		words = item.split()
		if len(words) < 1:
			continue
		NewIP = socket.gethostbyname(words[0])
		print(words[0] + " - " + NewIP)
		try:
    			response = urlopen("http://" + words[0],timeout=2)
		except:
			print("[ERROR] http://" +  words[0] + " IP mismatch: " + words[1] + " " + NewIP)
		NewStr += words[0] + "\t" + NewIP + "\n"
	file_.seek(0)
	file_.write(NewStr)


