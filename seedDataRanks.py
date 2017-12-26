import pandas as pd
from riotwatcher import RiotWatcher
import time


key = #insert key here
region = "na1"

watcher = RiotWatcher(key)


def getName(id):
    return watcher.league.by_summoner(region, id)


df = pd.DataFrame.from_csv('seedData2.csv')


ranks = list()
other_playersIds = list()
other_playerNames = list()
other_ranks = list()

count = 1

for ids in df["summonerIds"]:
    if (count % 100) == 0:
        print("sleeping for 60 seconds")
        time.sleep(60)
    count = count + 1
    print(count)

    data = getName(ids)

    if len(data) == 0:
        ranks.append("NA")
    else:
        ranks.append(data[0]["tier"])
        for entry in data[0]["entries"]:
            other_playersIds.append(entry["playerOrTeamId"])
            other_playerNames.append(entry["playerOrTeamName"])
            other_ranks.append(data[0]["tier"])

df["rank"] = ranks

df.to_csv('seedData3.csv')

c = {"summonerIds": other_playersIds, "name": other_playerNames, "rank": other_ranks}
dfc = pd.DataFrame(data=c)
dfc.to_csv('otherPlayers.csv')
