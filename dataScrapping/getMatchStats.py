import pandas as pd
from riotwatcher import RiotWatcher
import time
from requests import HTTPError

key = #insert key here
region = "na1"

watcher = RiotWatcher(key)


def recentMatches(id):
    return watcher.match.by_id(region, id)

def saveData(name): #Saves Data to matchData(name).csv
    savedata = {"queue":queueType, "champion": champions, "role": role, "ranks": ranks, "visionScore": visionScores,
                         "wardsPlaced": wardsPlaced, "sightWardsBoughtInGame": sightWardsBoughtInGame,
                         "damageDealtToTurrets": damageDealtToTurrets, "totalDamageDealtToChampions": totalDamageDealtToChampions,
                         "physicalDamageDealtToChampions": physicalDamageDealtToChampions, "magicDamageDealtToChampions": magicDamageDealtToChampions,
                         "largestMultiKill": largestMultiKill, "totalTimeCrowdControlDealt": totalTimeCrowdControlDealt, 
                         "trueDamageDealtToChampions": trueDamageDealtToChampions, "firstBloodKill": firstBloodKill,
                         "goldEarned": goldEarned, "pentaKills": pentaKills, "timeCCingOthers": timeCCingOthers,
                         "win": win, "kda": kda, "perkStyles": perkStyles,
                        "perk0": perk0, "perk1": perk1, "perk2": perk2, "perk3": perk3, "perk4": perk4, "perk5": perk5}
    df = pd.DataFrame(data=savedata)
    ordered = df[["champion", "ranks", "visionScore", "wardsPlaced", "sightWardsBoughtInGame",
                "damageDealtToTurrets", "totalDamageDealtToChampions", "physicalDamageDealtToChampions", "magicDamageDealtToChampions",
                "largestMultiKill", "totalTimeCrowdControlDealt", "trueDamageDealtToChampions", "firstBloodKill", 
                "goldEarned", "pentaKills", "timeCCingOthers", "win", "kda", "perkStyles", 
                "perk0", "perk1", "perk2", "perk3", "perk4", "perk5"]]
    ordered.to_csv('matchData'+str(name)+'.csv')


df = pd.DataFrame.from_csv('matchData.csv', encoding='latin-1') 

count = 0
total = len(df['gameIds'])

(champions, ranks, visionScores, wardsPlaced, sightWardsBoughtInGame,
damageDealtToTurrets, totalDamageDealtToChampions,
physicalDamageDealtToChampions, magicDamageDealtToChampions, largestMultiKill,
totalTimeCrowdControlDealt, trueDamageDealtToChampions, firstBloodKill,
goldEarned, pentaKills, timeCCingOthers, win, kda,
perk0, perk1, perk2, perk3, perk4, perk5,
perkStyles) = ([] for i in range(25))

role = list()
queueType = list()

skipped = list()

try:
    for game in df['gameIds']:
        if (count % 100) == 0:
            print("sleeping for 120 seconds, data saving")
            saveData("save")
            time.sleep(120)
        print(count, "/", total," gameId = ", game)
        count = count + 1
        try:
            match = recentMatches(game)

            for player in match["participants"]:
                try:
                    stat = player["stats"]
                    try:
                        try:
                            role.append(player["timeline"]["lane"])
                        except KeyError:
                            role.append("NA")
                        try:
                            champions.append(player["championId"])
                        except KeyError:
                            champions.append("NA")
                        try:
                            ranks.append(player["highestAchievedSeasonTier"])
                        except KeyError:
                            ranks.append("NA")
                        try:
                            queueType.append(match["queueId"])
                        except KeyError:
                            queueType.append("NA")
                        try:
                            visionScores.append(stat["visionScore"])
                        except KeyError:
                            visionScores.append(0)
                        try:
                            sightWardsBoughtInGame.append(stat["sightWardsBoughtInGame"])
                        except KeyError:
                           sightWardsBoughtInGame.append(0) 
                        try:
                            damageDealtToTurrets.append(stat["damageDealtToTurrets"])
                        except KeyError:
                            damageDealtToTurrets.append(0)
                        try:
                            totalDamageDealtToChampions.append(stat["totalDamageDealtToChampions"])
                        except KeyError:
                            totalDamageDealtToChampions.append(0)
                        try:
                            physicalDamageDealtToChampions.append(stat["physicalDamageDealtToChampions"])
                        except KeyError:
                            physicalDamageDealtToChampions.append(0)
                        try:
                            magicDamageDealtToChampions.append(stat["magicDamageDealtToChampions"])
                        except KeyError:
                            magicDamageDealtToChampions.append(0)
                        try:
                            largestMultiKill.append(stat["largestMultiKill"])
                        except KeyError:
                            largestMultiKill.append(0)
                        try:
                            totalTimeCrowdControlDealt.append(stat["totalTimeCrowdControlDealt"])
                        except KeyError:
                            totalTimeCrowdControlDealt.appen(0)
                        try:
                            trueDamageDealtToChampions.append(stat["trueDamageDealtToChampions"])
                        except KeyError:
                            trueDamageDealtToChampions.append(0)
                        try:
                            goldEarned.append(stat["goldEarned"])
                        except KeyError:
                            goldEarned.append(0)
                        try:
                            pentaKills.append(stat["pentaKills"])
                        except KeyError:
                            pentaKills.append(0)
                        try:
                            timeCCingOthers.append(stat["timeCCingOthers"])
                        except KeyError:
                            timeCCingOthers.append(0)
                        try:
                            win.append(stat["win"])
                        except KeyError:
                            win.append("NA")
                        try:
                            kda.append([stat["kills"], stat["deaths"], stat["assists"]])
                        except KeyError:
                            kda.append("NA")
                        try:
                            firstBloodKill.append(stat["firstBloodKill"])
                        except KeyError:
                            firstBloodKill.append("NA")
                        try:
                            wardsPlaced.append(stat["wardsPlaced"])
                        except KeyError:
                            wardsPlaced.append(0)
                        try:
                            perk0.append([stat["perk0"], stat["perk0Var1"]])
                        except KeyError:
                            perk0.append("NA")
                        try:
                            perk1.append([stat["perk1"], stat["perk1Var1"]])
                        except KeyError:
                            perk1.append("NA")
                        try:
                            perk2.append([stat["perk2"], stat["perk2Var1"]])
                        except KeyError:
                            perk2.append("NA")
                        try:
                            perk3.append([stat["perk3"], stat["perk3Var1"]])
                        except KeyError:
                            perk3.append("NA")
                        try:
                            perk4.append([stat["perk4"], stat["perk4Var1"]])
                        except KeyError:
                            perk4.append("NA")
                        try:
                            perk5.append([stat["perk5"], stat["perk5Var1"]])
                        except KeyError:
                            perk5.append("NA")
                        try:
                            perkStyles.append([stat["perkPrimaryStyle"], stat["perkSubStyle"]])
                        except KeyError:
                            perkStyles.append("NA")
                           
                    except KeyError as er:
                        print("Stats were not avaiable for game id", game, "because of key, ", er)
                        skipped.append(player)

                        
                except KeyError:
                    print("player id, ", player, "had no stats")


        except HTTPError as err:
            print("skipped id ", game, "as there was no data")
            skipped.append(game)
            print("skipped these games so far ", skipped)

        if(count % 5000) == 0 :
            saveData(count)

    saveData("completed")

except HTTPError as err:
    print("caught error, ", err, "at id ", count)
    saveData("error")

except KeyboardInterrupt as err:
    print("Process interrupted, data is saved at count", count)
    saveData("interrupted")

print("skipped games", skipped)
