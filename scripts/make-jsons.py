import os
import os.path
import glob
import json
import sys
import re
import datetime
import csv
import hashlib

f = open("vocefiscal-jotform.csv", "r", encoding="iso-8859-1")
reader = csv.reader(f, delimiter=",")
first = False
for row in reader:
	if first == False:
		first = True
		continue
	d = dict()
	d["estado"] = row[3]
	d["municipio"] = row[4].upper()
	d["zonaEleitoral"] = ""
	d["secaoEleitoral"] = ""
	for i in range(len(row[6]),4):
		d["zonaEleitoral"] += "0"
	d["zonaEleitoral"] += row[6]
	for i in range(len(row[7]),4):
		d["secaoEleitoral"] += "0"
	d["secaoEleitoral"] += row[7]
	epoch = datetime.datetime.utcfromtimestamp(0)
	delta = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S") - epoch
	d["data"] = int(delta.total_seconds())
	list = str.replace(row[8], "http://www.jotform.com/uploads/", "https://vocefiscal-poll-tape-uploads-jotform.s3.amazonaws.com/")
	d["pictureURLList"] = list.split(" |")
	j = json.dumps(d, sort_keys=True)
	print(j)
	h = hashlib.md5()
	h.update(str(j).encode('utf-8'))
	print(h.hexdigest())
	g = open(str(h.hexdigest()) + ".json", "w", encoding="iso-8859-1")
	g.write(j)
	g.close()
