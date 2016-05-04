import csv
import os
from process_spreadsheet import process_spreadsheet
from debugging_image import debugging_image
from report_faulty_lines import report_faulty_lines
from writeToCSV import writeToCSV
from trackTeamStats import trackTeamStats

dataDir = "data"
newDataDir = "Workspace"
outfile = open(newDataDir + "/processedPlayerData.csv", 'w')
teamOutfile = open(newDataDir + "/processedTeamData.csv", 'w')
for filename in os.listdir(dataDir):
	if filename[len(filename)-4:] != ".csv":
		continue
	[players, successLines] = process_spreadsheet(dataDir+"/"+filename)
	team = filename[:len(filename)-4]
	
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