import csv
import os
from process_spreadsheet import process_spreadsheet
from debugging_image import debugging_image
from report_faulty_lines import report_faulty_lines
from writeToCSV import writeToCSV

dataDir = "data"
playersOutputFile = "processedPlayerData.csv"
teamsOutputFile   = "processedTeamData.csv"
newDataDir = "Workspace"

outfileLocation = newDataDir + "/" + playersOutputFile
outfile = open(outfileLocation, 'w')
for filename in os.listdir(dataDir):
	if filename[len(filename)-4:] != ".csv":
		continue
	[players, successLines] = process_spreadsheet(dataDir+"/"+filename)
	team = filename[:len(filename)-4]
	
	writeToCSV(players, outfile, team)
	
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
	#do stuff to players (Either store them temporarily or put them in
	#the csv right away, I haven't thought this through yet)