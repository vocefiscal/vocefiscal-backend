import sys
import csv

state = sys.argv[1]
r = open("%s/r.txt" % state, 'r')
s = open("%s/s.txt" % state, 'r')
reader1 = csv.reader(r, delimiter=";")
reader2 = csv.reader(s, delimiter=";")
list = []
for row1 in reader1:
	s.seek(0)
	for row2 in reader2:
		if row1[0] == row2[0] and row1[2] == row2[2] and row1[3] == row2[3] and row1[4] == row2[5] and int(row1[5]) == int(row2[6]):
			list.append(row1)
r.seek(0)
for row1 in reader1:
	found = 0
	s.seek(0)
	for row2 in reader2:
		if row2[5] == row1[4]:
			found = 1
	if (found == 0):
		list.append(row1)
r.seek(0)
for row1 in reader1:
	found = 0;
	for row in list:
		if row1[0] == row[0] and row1[1] == row[1] and row1[2] == row[2] and row1[3] == row[3] and row1[4] == row[4]:
			found = 1
	if (found == 0 and int(row1[4]) > 0):
		print(row1)
