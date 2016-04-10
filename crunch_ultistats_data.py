import csv
import os
from process_spreadsheet import process_spreadsheet

dataDir = "data"
for filename in os.listdir(dataDir):
	players = process_spreadsheet(dataDir+"/"+filename)
	print players
	#do stuff to players