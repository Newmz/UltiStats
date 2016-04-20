import csv
import os
from process_spreadsheet import process_spreadsheet

def writeToCSV(players, playerName):
	outstr = ''
	outstr += playerName + ","
	outstr += str(len(players[playerName]["gameDates"])) + ","
	outstr += str(players[playerName]["secondsPlayed"]) + ","
	outstr += str(players[playerName]["OPoints"]) + ","
	outstr += str(players[playerName]["OPointConversions"]) + ","
	outstr += str(players[playerName]["DPoints"]) + ","
	outstr += str(players[playerName]["DPointConversions"]) + ","
	outstr += str(players[playerName]["touches"]) + ","
	outstr += str(players[playerName]["throws"]) + ","
	outstr += str(players[playerName]["catches"]) + ","
	outstr += str(players[playerName]["goals"]) + ","
	outstr += str(players[playerName]["assists"]) + ","
	outstr += str(players[playerName]["pulls"]) + ","
	if players[playerName]["timedPulls"] == 0:
		outstr += "0,"
	else:
		outstr += str(players[playerName]["pullHangtime"]/players[playerName]["timedPulls"]) + ","
	outstr += str(players[playerName]["callahansFor"]) + ","
	outstr += str(players[playerName]["callahansAgainst"]) + ","
	outstr += str(players[playerName]["stalls"]) + ","
	outstr += str(players[playerName]["throwaways"]) + ","
	outstr += str(players[playerName]["drops"]) + ","
	outstr += str(players[playerName]["OB Pulls"]) + ","
	outstr += str(players[playerName]["penalties"])
	return outstr


dataDir = "data"
for filename in os.listdir(dataDir):
	[players, successLines] = process_spreadsheet(dataDir+"/"+filename)
	print "hello"
	print "name,games,seconds played,O Points,O Conversions,D Points,D Conversions,touches,throws,catches,goals,assists,pulls,pull\
	 hangtime,callies,bad callies,stalls,throwaways,drops,OB Pulls,penalties(turnover)"
	for playerName in players:
		print writeToCSV(players, playerName)
		#currently printing for debugging purposes but once this is done we can write to a csv
		# print playerName + " played " + str(len(players[playerName]["gameDates"])) + " games"
		# print playerName + " played " + str(players[playerName]["secondsPlayed"]) + " seconds"
		# print playerName + " played " + str(players[playerName]["OPoints"]) + " O-points"
		# print playerName + " converted " + str(players[playerName]["OPointConversions"]) + " of these"
		# print playerName + " played " + str(players[playerName]["DPoints"]) + " D-points"
		# print playerName + " converted " + str(players[playerName]["DPointConversions"]) + " of these"
		# print playerName + " had " + str(players[playerName]["touches"]) + " touches"
		# print playerName + " had " + str(players[playerName]["pulls"]) + " pulls"
		# if players[playerName]["timedPulls"]!=0:
		# 	print playerName + " had their pulls hang an average of " + str(players[playerName]["pullHangtime"]/players[playerName]["timedPulls"]) +" seconds"
		# print playerName + " had " + str(players[playerName]["goals"]) + " goals"
		# print playerName + " had " + str(players[playerName]["assists"]) + " assists"
		# print playerName + " had " + str(players[playerName]["catches"]) + " catches"
	goodlines = 0
	badlines = 0
	totallines = 0
	for thing in successLines:
		if (thing):
			goodlines += 1
		else:
			badlines += 1
		totallines += 1
	print str(goodlines) + "/" + str(totallines) + " successful lines parsed"

	#do stuff to players (Either store them temporarily or put them in
	#the csv right away, I haven't thought this through yet)