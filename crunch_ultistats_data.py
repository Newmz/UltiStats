import csv
import os
from process_spreadsheet import process_spreadsheet

dataDir = "data"
for filename in os.listdir(dataDir):
	players = process_spreadsheet(dataDir+"/"+filename)
	print "hello"
	for playerName in players:
		print playerName + " played " + str(len(players[playerName]["gameDates"])) + " games"
	#do stuff to players (Either store them temporarily or put them in
	#the csv right away, I haven't thought this through yet)