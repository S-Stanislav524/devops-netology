#!/usr/bin/env python3
import os
import socket
import pickle
with open("./test.txt", "r+w") as _file:
	NewSrv = {}
	for str in _file.readlines():
		key,val = str.strip().split(':')
		NewIP = socket.gethostbyname(key)
		print(key + " - " + NewIP)
		if (NewIP != val):
			print("[ERROR] http://" + key  + " IP mismatch: " + val + " " + NewIP)
		NewSrv[key] = NewIP
	_file.seek(0)
	for key,vai in NewSrv.items():
		_file.write('{}:{}\n'.format(key,val))


