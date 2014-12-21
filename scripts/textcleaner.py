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
	os.system("cp %s/%s ./%s.jpg" % (path, file, tape))
	os.system("../../textcleaner -g -e none -f 10 -o 5 %s.jpg _%s.jpg" % (tape, tape))
print("BUs errados: %d" % wrong)

