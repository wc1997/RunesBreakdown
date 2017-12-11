from riotwatcher import RiotWatcher

key = raw_input("Input API key")

watcher = RiotWatcher(key)
challenger = watcher.league.challenger_by_queue("na1", "RANKED_SOLO_5x5")
print(challenger['tier'])

challenger_Ids = list()
challenger_name = list()
challenger_accountIds = list()
for key in challenger['entries']:
    challenger_Ids.append(key['playerOrTeamId'])
    challenger_name.append(key['playerOrTeamName'])


print(challenger_Ids[1])
print(challenger_name[1])

print(watcher.match.matchlist_by_account_recent("na1", watcher.summoner.by_id(challenger_Ids[1])))
