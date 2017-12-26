import pandas as pd
from riotwatcher import RiotWatcher
import time
from requests import HTTPError

key = #insert key
region = "na1"

watcher = RiotWatcher(key)


def recentMatches(id):
    return watcher.match.matchlist_by_account_recent(region, id)


df = pd.DataFrame.from_csv('mergedData.csv', encoding='latin-1')

count = 1
total = len(df['accountIds'])
gameIds = list()
timeStamps = list()
queues = list()
seasons = list()
skipped = list()

try:
    for account in df['accountIds']:
        if (count % 100) == 0:
            print("sleeping for 60 seconds")
            time.sleep(60)
        print(count, "/", total)
        count = count + 1
        try:
            recent = recentMatches(account)
            for match in recent["matches"]:
                gameIds.append(match["gameId"])
                timeStamps.append(match["timestamp"])
                queues.append(match["queue"])
                seasons.append(match["season"])
        except HTTPError as err:
            print("skipped id ", account, "as there was no data")
            skipped.append(account)
            print("skipped these accounts so far ", skipped)

    c = {"gameIds": gameIds, "timeStamps": timeStamps, "queues": queues, "seasons": seasons}
    df = pd.DataFrame(data=c)
    ordered = df[["gameIds", "timeStamps", "queues", "seasons"]]
    ordered.to_csv('matchData.csv')

except HTTPError as err:
    print("caught error at id ", count)
    c = {"gameIds": gameIds, "timeStamps": timeStamps, "queues": queues, "seasons": seasons}
    df = pd.DataFrame(data=c)
    ordered = df[["gameIds", "timeStamps", "queues", "seasons"]]
    ordered.to_csv('matchDataErrored.csv')
