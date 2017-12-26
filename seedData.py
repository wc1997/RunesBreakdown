import json
import pandas as pd
from riotwatcher import RiotWatcher
import time


key = #
region = "na1"

watcher = RiotWatcher(key)

infile = open("matches10.json", 'r')
data = infile.read()
jsondata = json.loads(data)

accountIds = list()
summonerIds = list()
Champ1 = list()
Champ1Points = list()
Champ2 = list()
Champ2Points = list()
Champ3 = list()
Champ3Points = list()
rank = list()
championscores = list()


def key_champions(id):
    return watcher.champion_mastery.by_summoner(region, id)


def get_scores(id):
    return watcher.champion_mastery.scores_by_summoner(region, id)


count = 0

for match in jsondata["matches"]:
    for players in match["participantIdentities"]:
        if players["player"]["accountId"] not in accountIds:
            accountIds.append(players["player"]["accountId"])
            summonerIds.append(players["player"]["summonerId"])

for ids in summonerIds:
    if (count % 100) == 0:
        print("sleeping for 60 seconds")
        time.sleep(60)
    count = count + 1
    print(count)
    scores = key_champions(ids)
    try:
        Champ1.append(scores[0]["championId"])
        Champ1Points.append(scores[0]["championPoints"])
    except IndexError:
        print("No champion 1 for id", ids)
        Champ1.append("NA")
        Champ1Points.append("NA")
    try:
        Champ2.append(scores[1]["championId"])
        Champ2Points.append(scores[1]["championPoints"])
    except IndexError:
        print("No champion 2 for id", ids)
        Champ2.append("NA")
        Champ2Points.append("NA")
    try:
        Champ3.append(scores[2]["championId"])
        Champ3Points.append(scores[2]["championPoints"])
    except IndexError:
        print("No champion 3 for id", ids)
        Champ3.append("NA")
        Champ3Points.append("NA")
    if (count % 100) == 0:
        print("sleeping for 60 seconds")
        time.sleep(60)
    count = count + 1
    championscores.append(get_scores(ids))

c = {"accountIds":accountIds, "summonerIds":summonerIds,"totalChampScores":championscores, "Champ1":Champ1,"Champ1Points":Champ1Points,"Champ2":Champ2,"Champ2Points":Champ2Points, "Champ3":Champ3, "Champ3Points":Champ3Points}
dfc = pd.DataFrame(data=c)

dfc.to_csv('seedDatatest.csv')
