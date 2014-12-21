import sys
import csv

state = sys.argv[1]
r = open("%s/r.txt" % state, 'r')
d = open("%s/d.txt" % state, 'r')
c = open("%s/c.txt" % state, 'w')
reader1 = csv.reader(r, delimiter=";")
reader2 = csv.reader(d, delimiter=";")
writer = csv.writer(c, delimiter=";",quoting=csv.QUOTE_ALL)
list = []
for row1 in reader1:
	found = 0
	d.seek(0)
	for row2 in reader2:
		if row1 == row2:
			found = 1
	if (found == 0):
		writer.writerow([row1[2],row1[3]])

