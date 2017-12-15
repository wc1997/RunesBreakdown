import pandas as pd
import numpy as np
from riotwatcher import RiotWatcher
import time

key = raw_input("Input API key")

region = "na1"

watcher = RiotWatcher(key)

df = pd.DataFrame.from_csv('masters_and_challengers2.csv')

Champ1 = list()
Champ1Points = list()
Champ2 = list()
Champ2Points = list()
Champ3 = list()
Champ3Points = list()


def key_champions(id):
    return watcher.champion_mastery.by_summoner(region,id)

count = 0

for ids in df["ids"]:
    if (count%100) == 0:
       print("sleeping for 60 seconds")
       time.sleep(60)
    print(count)
    count = count+1
    scores = key_champions(ids)
    try :
        Champ1.append(scores[0]["championId"])
        Champ1Points.append(scores[0]["championPoints"])
    except IndexError:
        print("No champion 1 for id", ids)
        Champ1.append("NA")
        Champ1Points.append("NA")
    try :
        Champ2.append(scores[1]["championId"])
        Champ2Points.append(scores[1]["championPoints"])
    except IndexError:
        print("No champion 2 for id", ids)
        Champ2.append("NA")
        Champ2Points.append("NA")
    try :
        Champ3.append(scores[2]["championId"])
        Champ3Points.append(scores[2]["championPoints"])
    except IndexError:
        print("No champion 3 for id", ids)
        Champ3.append("NA")
        Champ3Points.append("NA")


df["Champ1"] = Champ1
df["Champ1 Points"] = Champ1Points
df["Champ2"] = Champ2
df["Champ2 Points"] = Champ2Points
df["Champ3"] = Champ3
df["Champ3 Points"] = Champ3Points

df.to_csv('masters_and_challengers3.csv')

