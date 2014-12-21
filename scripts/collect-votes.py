import os
import os.path
import glob
import json
import sys
import re

root = os.getcwd()
states = filter(os.path.isdir, os.listdir(os.getcwd()))
for state in states:
	if state != sys.argv[1]:
		continue
	os.chdir("%s/ok" % state)
	for city in glob.glob("*"):
		os.chdir(city)
		for zone in glob.glob("*"):
			os.chdir(zone)
			for section in glob.glob("*"):
				os.chdir(section)
				for tape in glob.glob("*.json"):
					if (os.path.isfile("%s.txt" % tape)):
						#print("%s.txt" % tape)
						f = open("%s.txt" % tape, 'r')
						pat = re.compile("[0-9][0-9]\s+[0-9][0-9][0-9][0-9]")
						for line in f:
							match = pat.search(line)
							if match:
								c = str.replace(city, "-", " ")
								text = match.group()
								text = text.split(" ")
								print("\"%s\";\"%s\";\"%d\";\"%d\";\"%s\";\"%s\"" % (state.upper(), c.upper(), int(zone), int(section), text[0], text[1]));
				os.chdir("..")
			os.chdir("..")
		os.chdir("..")
