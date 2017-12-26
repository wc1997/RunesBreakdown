import pandas as pd
from riotwatcher import RiotWatcher
import time


key = #insert key
region = "na1"

watcher = RiotWatcher(key)


def getName(id):
    return watcher.summoner.by_id(region, id)["name"]


df = pd.DataFrame.from_csv('seedDatatest.csv')


playernames = list()

count = 0

for ids in df["summonerIds"]:
    if (count % 100) == 0:
        print("sleeping for 60 seconds")
        time.sleep(60)
    count = count + 1
    playernames.append(getName(ids))

df["name"] = playernames

df.to_csv('seedData2.csv')
