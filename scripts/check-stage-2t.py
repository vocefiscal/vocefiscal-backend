import os, sys
import glob
import json, csv
import string
import subprocess
import shlex
import re

wrong = 0
root = os.getcwd()
for tape in glob.glob("*.json"):
	json_data=open(tape)
	data = json.load(json_data)
	first = data["pictureURLList"][0]
	first = str.replace(first, "%3A", ":")
	file = str.replace(first, "https://vocefiscal-poll-tape-uploads.s3.amazonaws.com/", "")
	path = "../../poll-tape-uploads/"
	os.system("cp %s/%s tmp.jpg" % (path, file))
	#os.system("../../textcleaner -g -e none -f 10 -o 5 tmp.jpg _tmp.jpg")
	cmd = "tesseract -l por %s/%s stdout bazaar letters" % (path, file)
	pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
	output = pipe.communicate()[0].decode("utf-8")
	json_data.close()
	os.system("xdg-open %s/%s" % (path, file))
	print(tape)
	print("Digite comando:")
	print()
	ch = sys.stdin.readline()
	if ch == "y\n":
		os.system("mv %s nok" % tape)
	if ch == "n\n":
		os.system("mv %s 1t" % tape)
	print()
print("BUs errados: %d" % wrong)

