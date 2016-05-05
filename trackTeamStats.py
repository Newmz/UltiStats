#This function takes all the players on a team and adds their stats 
#together

def trackTeamStats(players, outfile, teamName):
	#sum the team statistics
	team = {}
	for playerName, player in players.iteritems():
		for statName, stat in player.iteritems():
			if statName in player:
				team[statName] = stat
			else:
				team[statName] += stat

	outstr = ''
	outstr += teamName + ","
	outstr += str(len(team["gameDates"])) + ","
	outstr += str(team["secondsPlayed"]) + ","
	outstr += str(team["OPoints"]) + ","
	outstr += str(team["OPointConversions"]) + ","
	outstr += str(team["DPoints"]) + ","
	outstr += str(team["DPointConversions"]) + ","
	outstr += str(team["touches"]) + ","
	outstr += str(team["throws"]) + ","
	outstr += str(team["catches"]) + ","
	outstr += str(team["goals"]) + ","
	outstr += str(team["assists"]) + ","
	outstr += str(team["pulls"]) + ","
	if team["timedPulls"] == 0:
		outstr += "0,"
	else:
		outstr += str(team["pullHangtime"]/team["timedPulls"]) + ","
	outstr += str(team["callahansFor"]) + ","
	outstr += str(team["callahansAgainst"]) + ","
	outstr += str(team["stalls"]) + ","
	outstr += str(team["throwaways"]) + ","
	outstr += str(team["drops"]) + ","
	outstr += str(team["OB Pulls"]) + ","
	outstr += str(team["penalties"])
	outstr += "\n"
	outfile.write(outstr)
	