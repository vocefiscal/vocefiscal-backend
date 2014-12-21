import os
import glob
import json
import string
import subprocess
import shlex
import re

wrong = 0
root = os.getcwd()
os.chdir("poll-tape-data")
for dir in glob.glob("*"):
	os.chdir("%s" % dir)
	os.chdir("br")
	for state in glob.glob("*"):
		os.chdir(state)
		for city in glob.glob("*"):
			os.chdir(city)
			for zone in glob.glob("*"):
				os.chdir(zone)
				for tape in glob.glob("*.json"):
					json_data=open(tape)
					data = json.load(json_data)
					right_zone = int(data["zonaEleitoral"])
					right_section = int(data["secaoEleitoral"])
					first = data["pictureURLList"][0]
					first = str.replace(first, "%3A", ":")
					file = str.replace(first, "https://vocefiscal-poll-tape-uploads.s3.amazonaws.com/", "")
					path = "../../../../../../poll-tape-uploads/"
					os.system("cp %s/%s tmp%s.jpg" % (path, file, right_zone))
					os.system("%s/textcleaner tmp%s.jpg _tmp%s.jpg" % (root, right_zone, right_zone))
					cmd = "tesseract --tessdata-dir %s -l por _tmp%s.jpg stdout bazaar letters" % (root, right_zone)
					pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
					output = pipe.communicate()[0].decode("utf-8")
					print("%d %d" % (right_zone, right_section))
					json_data.close()
					municipio = data["municipio"][0:5]
					pat = re.compile(municipio)
					match = pat.search(output)
					#os.system("rm tmp.jpg _tmp.jpg")
					if not match:
						wrong = wrong + 1
						print(first)
					else:
						print(data["municipio"])
				os.chdir("../")
			os.chdir("../")
		os.chdir("../")
	os.chdir("../../")
print("BUs errados: %d" % wrong)

