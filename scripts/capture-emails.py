import os
import glob
import json

for tape in glob.glob("*.json"):
	json_data=open(tape, "r")
	data = json.load(json_data)
	if "email" in data.keys():
		print(data["email"])
	json_data.close()
