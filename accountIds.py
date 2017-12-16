import pandas as pd
import numpy as np
from riotwatcher import RiotWatcher
import time


key = raw_input("Input API key")

region = "na1"

watcher = RiotWatcher(key)

df = pd.DataFrame.from_csv('masters_and_challengers3.csv')

accountIds = list()

def account_id(id):
    return watcher.summoner.by_id(region,id)["accountId"]
    
count = 0


for ids in df["ids"]:
    if (count%100) == 0:
       print("sleeping for 60 seconds")
       time.sleep(60)
    print(count)
    count = count+1
    accountIds.append(account_id(ids))
   


df["accountId"] = accountIds


df.to_csv('masters_and_challengers4.csv')
