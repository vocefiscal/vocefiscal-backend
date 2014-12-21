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
	print(tape)
	json_data=open(tape)
	data = json.load(json_data)
	first = data["pictureURLList"][0]
	first = str.replace(first, "%3A", ":")
	file = str.replace(first, "https://vocefiscal-poll-tape-uploads.s3.amazonaws.com/", "")
	path = "../../poll-tape-uploads/"
	#os.system("cp %s/%s tmp.jpg" % (path, file))
	#os.system("../../textcleaner tmp.jpg _tmp.jpg")
	cmd = "tesseract -l por %s/%s stdout bazaar letters" % (path, file)
	pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
	output = pipe.communicate()[0].decode("utf-8")
	json_data.close()
	pat = re.compile("^[O|0-9]\s*[O|0-9]\s*[O|0-9]\s*[\.|\:]\s*[O|0-9]\s*[O|0-9]\s*[O|0-9]", flags=re.MULTILINE)
	match = pat.search(output)
	os.system("rm tmp.jpg")
	print(tape)
	if not match:
		wrong = wrong + 1
		print("NAO IDENTIFICADO")
		print(first)
		print(data["municipio"])
		print(data["zonaEleitoral"])
		print(data["secaoEleitoral"])
		os.system("mv %s nok" % tape)
	else:
		corr = match.group();
		corr = str.replace(corr, "O", "0")
		corr = str.replace(corr, ":", ".")
		corr = str.replace(corr, " ", "")
		print(corr)
		for ceft in glob.glob("../../ceft/ceft_1t_%s_*.txt" % data["estado"]):
			with open(ceft, "r", encoding="iso-8859-1") as f:
				reader=csv.reader(f, delimiter=";")
				found = 0
				for row in reader:
					if row[8] and row[9]:
						if int(data["zonaEleitoral"]) == int(row[7]) and int(data["secaoEleitoral"]) == int(row[8]) and data["municipio"] == row[6] and corr == row[13]:
							print("IDENTIFICADO")
							os.system("mv %s ok" % tape)
							found = 1

				if found == 0:
					wrong = wrong + 1
					print("NAO IDENTIFICADO")
					print(first)
					print(data["municipio"])
					print(data["zonaEleitoral"])
					print(data["secaoEleitoral"])
					os.system("mv %s nok" % tape)
		print()
print("BUs errados: %d" % wrong)

