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
					#trackTouches(players, line, previousLine)
					a = None
				
				if line[12]!="" or line[5]!=previousLine[5] or line[6]!=previousLine[6]:
						#put all statistics that only get counted once per point here
						trackSeconds(players, line)
						trackOPoints(players, line)
						trackDPoints(players, line)
						trackOConversions(players, line, previousLine)
						trackDConversions(players, line, previousLine)
						trackPulls(players, line)
						trackPullHangtime(players, line)
				#this is the last thing we do each loop
				previousLine = line
		except Exception as inst:
			print inst.args
	return players			

#process_spreadsheet("AH2015.csv")

#a touch is recorded when:
#	a player picks up/catches a pull
#	a player catches a pass (including for a score)
#	a callahan
# this function can easily be modified to track goals/assists/catches.

def trackTouches(players, line, previousLine):
	#cally
	if line[7] == "Defense" and line[8] == "Callahan":
		#print line[11] + " +1 touch (callahan)"
		pname = line[11]
		players[pname]["touches"] += 1
	#cally is the only way to get a touch when line[7] == "defense",
	# so we can continue
	if line[7] != "Offense":
		return
	#the only way I found out to find if it was from a pull is if
	#	previousLine[7] == Defense && previousLine[8] == Goal OR
	#	previousLine[7] == Cessation && line[7] == Offense.
	#in this case, add a touch for the person throwing AND the person catching.
	if (previousLine[7] == "Defense" and previousLine[8] == "Goal") or \
	 (previousLine[7] == "Cessation" and line[7] == "Offense"):
		#print  line[9] + " +1 touch (pull)"
		pname = line[9]
		players[pname]["touches"] += 1
	if line[8] == "Goal":
		#print line[10] + " +1 touch (goal)"
		pname = line[10]
		players[pname]["touches"] += 1

	elif line[8] == "Catch":
		#print line[10] + " +1 touch(catch)"
		pname = line[10]
		players[pname]["touches"] += 1


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
			players[playerName]["OPoints"] = 0
			players[playerName]["DPoints"] = 0
			players[playerName]["OPointConversions"] = 0
			players[playerName]["DPointConversions"] = 0
			players[playerName]["touches"] = 0
			players[playerName]["pulls"] = 0
			players[playerName]["pullHangtime"] = 0
			players[playerName]["timedPulls"] = 0

def trackSeconds(players, line):
	playerZeroIndex = 13
	playerSixIndex  = 19
	for playerIndex in range(playerZeroIndex, playerSixIndex):
		playerName = line[playerIndex]
		players[playerName]["secondsPlayed"]+=int(line[3])

def trackOPoints(players, line):
	playerZeroIndex = 13
	playerSixIndex  = 19
	if line[4]=="O":
		for playerIndex in range(playerZeroIndex, playerSixIndex):
			playerName = line[playerIndex]
			players[playerName]["OPoints"]+=1

def trackDPoints(players, line):
	playerZeroIndex = 13
	playerSixIndex  = 19
	if line[4]=="D":
		for playerIndex in range(playerZeroIndex, playerSixIndex):
			playerName = line[playerIndex]
			players[playerName]["DPoints"]+=1

def trackOConversions(players, line, previousLine):
	playerZeroIndex = 13
	playerSixIndex  = 19
	if line[4]=="O":
		#check if we scored this O-point
		if (previousLine == None and line[5]=="1") or int(line[5])==int(previousLine[5])+1:
			for playerIndex in range(playerZeroIndex, playerSixIndex):
				playerName = line[playerIndex]
				players[playerName]["OPointConversions"]+=1

def trackDConversions(players, line, previousLine):
	playerZeroIndex = 13
	playerSixIndex  = 19
	if line[4]=="D":
		#check if we scored this O-point
		if (previousLine == None and line[5]=="1") or int(line[5])==int(previousLine[5])+1:
			for playerIndex in range(playerZeroIndex, playerSixIndex):
				playerName = line[playerIndex]
				players[playerName]["DPointConversions"]+=1

def trackPulls(players, line):
	if line[11]!="":
		players[line[11]]["pulls"]+=1
	else:
		print "No one to give this pull to"

def trackPullHangtime(players, line):
	#if the puller was tracked
	if line[11]!="":
		#if the hangtime was tracked
		if line[12]:
			players[line[11]]["pullHangtime"]+=float(line[12])
			players[line[11]]["timedPulls"]+=1
