#!/usr/bin/python

import os

extensions = ['js', 'css', 'php', 'html']
continue_list = ['y', 'yes', 'Y', 'Yes', 'YES']

path = os.getcwd()

print "Your current path: " + path

rootdir = raw_input("Enter the root directory: ")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
	newFile =  file.split('.')
	if len(newFile) > 1:
		if newFile[1] in extensions:
			print "Files that will be converted: " + os.path.join(subdir, file)

convert = raw_input("Do you want to convert these files? (yes/no)")

if convert in continue_list:
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
        		newFile =  file.split('.')
        		if len(newFile) > 1:
                		if newFile[1] in extensions:
					print "File converted to: " + newFile[0] + '_' + newFile[1] + ".txt"
