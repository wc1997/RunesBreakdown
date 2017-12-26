from riotwatcher import RiotWatcher
import pandas as pd
import numpy as np


key = raw_input("Input API key")

region = "na1"

watcher = RiotWatcher(key)
challenger = watcher.league.challenger_by_queue(region, "RANKED_SOLO_5x5")
masters = watcher.league.masters_by_queue(region, "RANKED_SOLO_5x5")

print(challenger['tier'])

challenger_Ids = list()
challenger_names = list()
challenger_accountIds = list()

masters_Ids = list()
masters_names = list()
masters_accountIds = list()

for key in challenger['entries']:
    challenger_Ids.append(key['playerOrTeamId'])
    challenger_names.append(key['playerOrTeamName'])

for key in masters['entries']:
    masters_Ids.append(key['playerOrTeamId'])
    masters_names.append(key['playerOrTeamName'])

c = {"ids": challenger_Ids, "name": challenger_names, "rank": "challenger"}
m = {"ids": masters_Ids, "name": masters_names, "rank": "master"}

dfc = pd.DataFrame(data=c)
dfm = pd.DataFrame(data=m)

frames = [dfc, dfm]
result = pd.concat(frames)
print(result)

result.to_csv('masters_and_challengers.csv')





#for i in range(1, len(challenger_Ids)):
#    challenger_accountIds.append(watcher.summoner.by_id(region,challenger_Ids[i])['accountId'])

#for i in range(1,len(masters_Ids)):
#    masters_accountIds.append(watcher.summoner.by_id(region,masters_Ids[i])['accountId'])

## Now we have Ids, accountIds, and names of each player in challenger and master

#print(challenger_accountIds)

# print(challenger_Ids[1])
# print(challenger_name[1])
# print(watcher.summoner.by_id("na1", challenger_Ids[1])['accountId'])

#print(watcher.match.matchlist_by_account_recent("na1",watcher.summoner.by_id("na1", challenger_Ids[1])['accountId']))
