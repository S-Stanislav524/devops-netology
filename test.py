#!/usr/bin/env python3
import os
from sys import argv
if len (argv) == 2:
        path = argv[1]
else:
        path = "./"
bash_cmd="cd " + path
bash_command = [bash_cmd, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if (result.find('modified') != -1):
         prepare_result = result.replace('\tmodified:   ', '')
         print(os.path.abspath(path + prepare_result))


