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
		print playerName + " had " + str(players[playerName]["touches"]) + " touches"
		print playerName + " had " + str(players[playerName]["pulls"]) + " pulls"
		if players[playerName]["timedPulls"]!=0:
			print playerName + " had their pulls hang an average of " + str(players[playerName]["pullHangtime"]/players[playerName]["timedPulls"]) +" seconds"
	#do stuff to players (Either store them temporarily or put them in
	#the csv right away, I haven't thought this through yet)
	outputFile = open(filename.split(".")[0]+"processed.csv", "w")
	outputFile.write("Player Name, Games Played, Seconds Played, O-points, O-point conversions, D-points, D-point conversions, Pulls, Timed Pulls, Pull Hangtime\n") 
	for playerName in players:
		print playerName
		if players[playerName]["timedPulls"]!=0:
			outputFile.write(playerName +"," +str(len(players[playerName]["gameDates"]))+","+str(players[playerName]["secondsPlayed"])+\
				"," + str(players[playerName]["OPoints"]) + "," + str(players[playerName]["OPointConversions"]) + "," +\
				str(players[playerName]["DPoints"]) + "," + str(players[playerName]["DPointConversions"])  + "," + \
				str(players[playerName]["pulls"]) + "," + str(players[playerName]["timedPulls"]) + "," +\
				str(players[playerName]["pullHangtime"]/players[playerName]["timedPulls"])+"\n")
		else:
			outputFile.write(playerName +"," +str(len(players[playerName]["gameDates"]))+","+str(players[playerName]["secondsPlayed"])\
				+ "," + str(players[playerName]["OPoints"]) + "," + str(players[playerName]["OPointConversions"]) + "," +\
				str(players[playerName]["DPoints"]) + "," + str(players[playerName]["DPointConversions"])  + "," + \
				str(players[playerName]["pulls"]) + "," + str(players[playerName]["timedPulls"]) + "," +\
				"-1\n")
	outputFile.close()
