def writeToCSV(players, outfile, teamName):
	outfile.write("Name,Games,Minutes Played,O Points,O Conversions,D Points,D Conversions,Touches,Throws,Catches,Goals,Assists,Pulls,Average Pull Hangtime,Callahans,Callahans Thrown,Stalls,Throwaways,Drops,Pulls OB,Penalties, Team\n")
	for playerName in players:	
		outstr = ''
		outstr += playerName + ","
		outstr += str(len(players[playerName]["gameDates"])) + ","
		outstr += str(players[playerName]["secondsPlayed"]/60.0) + ","
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
