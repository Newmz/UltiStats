import csv
import os
from process_spreadsheet import process_spreadsheet

dataDir = "data"
for filename in os.listdir(dataDir):
	players = process_spreadsheet(dataDir+"/"+filename)
	print "hello"
	for playerName in players:
		#currently printing for debugging purposes but once this is done we can write to a csv
		print playerName + " played " + str(len(players[playerName]["gameDates"])) + " games"
		print playerName + " played " + str(players[playerName]["secondsPlayed"]) + " seconds"
		print playerName + " played " + str(players[playerName]["OPoints"]) + " O-points"
		print playerName + " converted " + str(players[playerName]["OPointConversions"]) + " of these"
		print playerName + " played " + str(players[playerName]["DPoints"]) + " D-points"
		print playerName + " converted " + str(players[playerName]["DPointConversions"]) + " of these"
	#do stuff to players (Either store them temporarily or put them in
	#the csv right away, I haven't thought this through yet)