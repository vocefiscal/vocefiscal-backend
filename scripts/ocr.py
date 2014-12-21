import os
import os.path
import glob
import json
import sys

root = os.getcwd()
states = filter(os.path.isdir, os.listdir(os.getcwd()))
for state in states:
	if state != sys.argv[1]:
		continue
	os.chdir("%s/ok" % state)
	for city in glob.glob("*"):
		for zone in glob.glob("%s/*" % city):
			for section in glob.glob("%s/*" % (zone)):
				for tape in glob.glob("%s/*.json" % section):
					if (os.path.isfile("%s.txt" % tape)):
						continue
					json_data=open(tape)
					data = json.load(json_data)
					os.system("rm %s.txt" % tape)
					for i in range(0, len(data["pictureURLList"])):
						pic = data["pictureURLList"][i]
						pic = str.replace(pic, "%3A", ":")
						file = str.replace(pic, "https://vocefiscal-poll-tape-uploads.s3.amazonaws.com/", "")
						path = "../../../poll-tape-uploads/"
						os.system("cp %s/%s %s/%02d.jpg" % (path, file, section, i))
						os.system("%s/../textcleaner -g -e none -f 10 -o 5 %s/%02d.jpg %s/_%02d.jpg" % (root, section, i, section, i))
						os.system("tesseract -l por %s/_%02d.jpg stdout >> %s.txt" % (section, i, tape))

