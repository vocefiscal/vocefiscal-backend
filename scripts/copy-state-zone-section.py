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
	json_data=open(tape)
	data = json.load(json_data)
	city = data["municipio"]
	zone = data["zonaEleitoral"]
	section = data["secaoEleitoral"]
	city = city.lower()
	city = str.replace(city, " ", "-")
	city = str.replace(city, "'", "\\'")
	if not os.path.exists("./%s/%s/%s" % (city,zone,section)):
		os.makedirs("./%s/%s/%s" % (city,zone,section))
	os.system("mv %s %s/%s/%s/" % (tape,city,zone,section))
	json_data.close()
