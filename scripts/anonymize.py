import os
import glob
import json

for tape in glob.glob("*.json"):
	print(tape)
	json_data=open(tape, "r")
	data = json.load(json_data)
	if "email" in data.keys():
		del data["email"]
	json_data.close()

	json_data=open(tape, "w+")
	json_data.write(json.dumps(data))
	json_data.close()
