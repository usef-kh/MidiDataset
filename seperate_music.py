import sys
from os import listdir, path, mkdir, system
from os.path import isfile, join, isdir
import re


def run_spleeter(d):
	if(not isdir(d)):
			print("Please provide a valid directory")
	else:
		files = [f for f in listdir(d) if isfile(join(d, f)) and '.mp3' in join(sys.argv[1], f)]
		for f in files:
			print("Running Spleeter for {0}".format(f))
			exit_code = system("spleeter separate -i \"{0}\" -o seperated".format(f))
			if(exit_code != 0):
				print("Spleeter failed for {0}".format(f))

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print("Improper arguments. Please follow the format. Python3 ./seperate_music.py <directory_location>")
	else:
		run_spleeter(sys.argv[1])




