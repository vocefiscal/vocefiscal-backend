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
	first = data["pictureURLList"][0]
	first = str.replace(first, "%3A", ":")
	file = str.replace(first, "https://vocefiscal-poll-tape-uploads.s3.amazonaws.com/", "")
	path = "../../poll-tape-uploads/"
	os.system("cp %s/%s tmp.jpg" % (path, file))
	os.system("../../textcleaner tmp.jpg _tmp.jpg")
	cmd = "tesseract --tessdata-dir %s -l por _tmp.jpg stdout bazaar letters" % root
	cmd = "tesseract -l por _tmp.jpg stdout bazaar letters"
	pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
	output = pipe.communicate()[0].decode("utf-8")
	json_data.close()
	estado = "\[%s" % data["estado"]
	pat = re.compile(estado)
	match = pat.search(output)
	os.system("rm tmp.jpg _tmp.jpg")
	if not match:
		estado = "%s\]" % data["estado"]
		pat = re.compile(estado)
		match = pat.search(output)
		if not match:
			print(tape)
			wrong = wrong + 1
			print("NAO IDENTIFICADO")
			print(first)
			print(data["zonaEleitoral"])
			print(data["secaoEleitoral"])
			print()
			os.system("mv %s nok" % tape)
		else:
			print(tape)
			print(match.group())
			print(first)
			print(data["zonaEleitoral"])
			print(data["secaoEleitoral"])
			print()
	else:
		print(tape)
		print(match.group())
		print(first)
		print(data["zonaEleitoral"])
		print(data["secaoEleitoral"])
		print()
print("BUs errados: %d" % wrong)

