import csv
import os
from process_spreadsheet import process_spreadsheet
from debugging_image import debugging_image
from report_faulty_lines import report_faulty_lines

def writeToCSV(players, playerName, outfile):
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
	outstr += "\n"
	outfile.write(outstr)


dataDir = "data"
for filename in os.listdir(dataDir):
	[players, successLines] = process_spreadsheet(dataDir+"/"+filename)
	outfile = filename[:len(filename)-4] + "_stats.csv"
	x = open(outfile, 'w')
	print "hello"
	x.write("name,games,seconds played,O Points,O Conversions,D Points,D Conversions,touches,throws,catches,goals,assists,pulls,pull\
	 hangtime,callies,bad callies,stalls,throwaways,drops,OB Pulls,penalties(turnover)\n")
	for playerName in players:
		writeToCSV(players, playerName, x)
	x.close()
#Handle stats on our stats!
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
	debuggingFileName = "debuggingImages/"+filename.split(".")[0]+"_debugger"
	debugging_image(successLines, debuggingFileName+".png")
	report_faulty_lines(successLines, debuggingFileName+".txt")

	#do stuff to players (Either store them temporarily or put them in
	#the csv right away, I haven't thought this through yet)