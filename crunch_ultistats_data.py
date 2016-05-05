import csv
import os
from process_spreadsheet import process_spreadsheet
from debugging_image import debugging_image
from report_faulty_lines import report_faulty_lines
from writeToCSV import writeToCSV
from trackTeamStats import trackTeamStats
import re

dataDir = "data"
newDataDir = "Workspace"
outfile = open(newDataDir + "/processedPlayerData.csv", 'w')
teamOutfile = open(newDataDir + "/processedTeamData.csv", 'w')
teamOutfile.write("name,games,seconds played,O Points,O Conversions,D Points,D Conversions,touches,throws,catches,goals,assists,pulls,pull hangtime,callies,bad callies,stalls,throwaways,drops,OB Pulls,penalties(turnover)")

for filename in os.listdir(dataDir):
	if filename[len(filename)-4:] != ".csv":
		continue
	[players, successLines] = process_spreadsheet(dataDir+"/"+filename)

	team = filename[:len(filename)-10]
	#print team
	teamWords = re.findall('[A-Z][^A-Z]*', team)
	print teamWords
	team = teamWords[0]
	for i,word in enumerate(teamWords):
		if word != team:
			print i
			if i == (len(teamWords)-1):
				team += " " + word[:len(filename)-4] + "  " + word[len(filename)-4:]
			else:
				team += " " + word
	print team
	
	writeToCSV(players, outfile, team)
	trackTeamStats(players, teamOutfile, team)
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
outfile.close()
teamOutfile.close()