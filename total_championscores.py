import pandas as pd
import numpy as np
from riotwatcher import RiotWatcher
import time


key = raw_input("Input API key")
region = "na1"

watcher = RiotWatcher(key)

df = pd.DataFrame.from_csv('masters_and_challengers.csv')
championscores = list()


def get_scores(id):
    return watcher.champion_mastery.scores_by_summoner(region,id)

count = 0

for ids in df["ids"]:
   print(ids)
   if (count%100) == 0:
        print("sleeping for 60 seconds")
        time.sleep(60)
   count = count+1
   championscores.append(get_scores(ids))

df["totalChampScores"] = championscores

df.to_csv('masters_and_challengers2.csv')

