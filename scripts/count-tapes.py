import os
import subprocess
import glob
import shlex

states = filter(os.path.isdir, os.listdir(os.getcwd()))
for state in states:
	if state != "testes":
		os.chdir(state)
		os.chdir("ok")
		ok = len(glob.glob("*.json"))
		os.chdir("..")
		os.chdir("nok")
		nok = len(glob.glob("*.json"))
		print("%s\t%d\t%d" % (state.upper(), nok+ok, ok))
		os.chdir("..")
		os.chdir("..")

