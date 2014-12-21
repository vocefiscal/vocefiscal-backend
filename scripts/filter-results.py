import os
import os.path
import glob
import json
import sys
import re
import csv

root = os.getcwd()
states = filter(os.path.isdir, os.listdir(os.getcwd()))
for state in states:
	if state != sys.argv[1]:
		continue
	os.chdir("%s/ok" % state)
	list = []
	for city in glob.glob("*"):
		os.chdir(city)
		for zone in glob.glob("*"):
			os.chdir(zone)
			for section in glob.glob("*"):
				list.append((int(zone),int(section)))
			os.chdir("..")
		os.chdir("..")
	os.chdir("../..")
	for results in glob.glob("../buweb/bweb_2t_%s_*.txt" % state.upper()):
		with open(results, "r", encoding="iso-8859-1") as r:
			reader = csv.reader(r, delimiter=";")
			for row in reader:
				for tuple in list:
					if int(row[7]) == int(tuple[0]) and int(row[8]) == int(tuple[1]):
						print("\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\"" % (row[4],row[6],row[7],row[8],row[13],row[21],row[23],row[17]))
