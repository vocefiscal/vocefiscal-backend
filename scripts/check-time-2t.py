import os
import glob
import json
import string
import subprocess
import shlex
import re

wrong = 0
root = os.getcwd()
for tape in glob.glob("*.json"):
	print(tape)
	json_data=open(tape)
	data = json.load(json_data)
	first = data["pictureURLList"][0]
	first = str.replace(first, "%3A", ":")
	time = int(data["data"])
	if time <= 1414346400000:
		print(first)
		os.system("mv %s ../testes" % tape)
	json_data.close()
