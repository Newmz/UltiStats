import csv

#this function takes a filepath to a spreadsheet from ultistats. It
#then computes statistics and returns them in players.
def process_spreadsheet(fname):
	players = {}
	#we open the csv and prepare to read it line by line
	with open(fname, 'rb') as csvfile:
		linereader = csv.reader(csvfile, delimiter="\n")
		header = next(linereader)
		#We have opened the file and read out the header. Now we read line
		#by line
		previousLine = None
		for line in linereader:
			#compute statistics here.
			if previousLine == None:
				#put all statistics that don't need previous line here
				a = "remove this once there is something here"
				#calculateExampleStatistic(line,players)
			else:
				#put all statistics that need the previous line here
				a = "remove this once there is something here"
				#calculateOtherExampleStatistic(line,previousLine, players)
			#this is the last thing we do each loop
			previousLine = line
	return players			

#process_spreadsheet("AtlantaHustle2016-stats.csv")