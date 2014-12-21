import os
import urllib.parse

f = open("vocefiscal-wget.txt")
content = f.readlines()
for line in content:
	line = str.replace(line, "http://", "./")
	line = str.replace(line, "%20", " ")
	line = str.replace(line, "\n", "")
	line = str.replace(line, "jpg ", "jpg")
	line = str.replace(line, "gif ", "gif")
	line = str.replace(line, "JPG ", "JPG")
	line = urllib.parse.unquote(line)
	if not os.path.isfile(line):
		print(line)
		#print(dir)
