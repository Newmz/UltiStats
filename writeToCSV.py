def writeToCSV(players, outfile, teamName):
	outfile.write("name,games,seconds played,O Points,O Conversions,D Points,D Conversions,touches,throws,catches,goals,assists,pulls,pull\
	 hangtime,callies,bad callies,stalls,throwaways,drops,OB Pulls,penalties(turnover),team\n")
	for playerName in players:	
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
		outstr += str(players[playerName]["penalties"]) + ","
		outstr += teamName
		outstr += "\n"
		outfile.write(outstr)
