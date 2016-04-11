import csv
import os

assumed_header = ['Date/Time,Tournamemnt,Opponent,Point Elapsed Seconds,Line,Our Score - End of Point,Their Score - End of Point,Event Type,Action,Passer,Receiver,Defender,Hang Time (secs),Player 0,Player 1,Player 2,Player 3,Player 4,Player 5,Player 6,Player 7,Player 8,Player 9,Player 10,Player 11,Player 12,Player 13,Player 14,Player 15,Player 16,Player 17,Player 18,Player 19,Player 20,Player 21,Player 22,Player 23,Player 24,Player 25,Player 26,Player 27,Elapsed Time (secs)']

#this function takes a filepath to a spreadsheet from ultistats. It
#then computes statistics and returns them in players.
def process_spreadsheet(fname):
	players = {}
	#we open the csv and prepare to read it line by line
	with open(fname, 'rb') as csvfile:
		linereader = csv.reader(csvfile, delimiter="\n")
		header = next(linereader)
		try:
			if header != assumed_header:
				raise Exception("Exception: the header is not what we thought")
			#We have opened the file and read out the header. Now we read line
			#by line
			previousLine = None
			for line_ in linereader:
				line = line_[0].split(",")
				#compute statistics here.
				#It is important that trackgames comes first as it is responsable
				#for instantiating players into the structure
				trackGames(players, line)
				if previousLine != None:
					#put all statistics that need previous line here
					a = None
				if line[12]!="" or line[5]!=previousLine[5] or line[6]!=previousLine[6]:
						#put all statistics that only get counted once per point here
						trackSeconds(players, line)
				#this is the last thing we do each loop
				previousLine = line
		except Exception as inst:
			print inst.args
	return players			

#process_spreadsheet("AtlantaHustle2016-stats.csv")

#If there is a player on this line who hasn't added this game to their
#stats yet add it
def trackGames(players, line):
	dateTime = line[0].split(" ")
	date = dateTime[0]
	playerZeroIndex = 13
	playerSixIndex  = 19
	for playerIndex in range(playerZeroIndex, playerSixIndex):
		playerName = line[playerIndex]
		if playerName in players:
			players[playerName]["gameDates"].add(date)
		else:
			players[playerName] = {"gameDates":set([date])}
			players[playerName]["secondsPlayed"]=0
	return

def trackSeconds(players, line):
	playerZeroIndex = 13
	playerSixIndex  = 19
	for playerIndex in range(playerZeroIndex, playerSixIndex):
		playerName = line[playerIndex]
		players[playerName]["secondsPlayed"]+=int(line[3])
	return