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
	found = 0
	for i in range(0, len(data["pictureURLList"])):
		if found == 1:
			break
		pic = data["pictureURLList"][len(data["pictureURLList"])-i-1]
		pic = str.replace(pic, "%3A", ":")
		file = str.replace(pic, "https://vocefiscal-poll-tape-uploads.s3.amazonaws.com/", "")
		path = "../../poll-tape-uploads/"
		os.system("cp %s/%s tmp.jpg" % (path, file))
		os.system("../../textcleaner tmp.jpg _tmp.jpg")
		cmd = "tesseract -l por _tmp.jpg stdout bazaar letters"# % (path, file)
		pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
		output = pipe.communicate()[0].decode("utf-8")
		pat = re.compile("^[O|0-9]\s*[O|0-9]\s*[O|0-9]\s*[\.|\:]\s*[O|0-9]\s*[O|0-9]\s*[O|0-9]s*[\.|\:]\s*[O|0-9]\s*[O|0-9]\s*[O|0-9]\s*", flags=re.MULTILINE)
		match = pat.search(output)
		os.system("rm tmp.jpg _tmp.jpg")
		print(pic)
		if not match:
			print(data["municipio"])
			print(data["zonaEleitoral"])
			print(data["secaoEleitoral"])
		else:
			code = match.group();
			code = str.replace(code, "O", "0")
			code = str.replace(code, ":", ".")
			code = str.replace(code, " ", "")
			print(code)
			for ceft in glob.glob("../../ceft_2t/ceft_2t_%s_*.txt" % data["estado"]):
				with open(ceft, "r", encoding="iso-8859-1") as f:
					reader=csv.reader(f, delimiter=";")
					for row in reader:
						if row[8] and row[9]:
							if int(data["zonaEleitoral"]) == int(row[7]) and int(data["secaoEleitoral"]) == int(row[8]) and data["municipio"] == row[6] and code == row[20][0:11]:
								print("IDENTIFICADO")
								json_data.close()
								os.system("mv %s ok" % tape)
								found = 1
								break
	if found == 0:
		print("NAO IDENTIFICADO")
		print(data["municipio"])
		print(data["zonaEleitoral"])
		print(data["secaoEleitoral"])
		json_data.close()
		os.system("mv %s nok" % tape)
	print()

