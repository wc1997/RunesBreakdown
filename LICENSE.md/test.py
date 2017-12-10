from riotwatcher import RiotWatcher

key = raw_input("Input API key")


watcher = RiotWatcher(key)
challenger = watcher.league.challenger_by_queue("na1", "RANKED_SOLO_5x5")
print(challenger['tier'])
for key in challenger['entries']:
	print(key['playerOrTeamName'])
