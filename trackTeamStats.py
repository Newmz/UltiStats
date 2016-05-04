#This function takes all the players on a team and adds their stats 
#together

def trackTeamStats(players):
	team = {}
	for playerName, player in players.iteritems():
		for statName, stat in player.iteritems():
			if statName in player:
				team[statName] = stat
			else:
				team[statName] += stat
	print team