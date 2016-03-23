import os
import sys
import fileinput

phrase = "CH"
filename= "iat-west-section-export.gpx"

for line in fileinput.input(filename, inplace=True):
    if phrase in line:
        continue
    print line,