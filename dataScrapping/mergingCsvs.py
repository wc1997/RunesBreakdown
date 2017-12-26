import pandas as pd

seedData = pd.DataFrame.from_csv('seedData3.csv')
challengerData = pd.DataFrame.from_csv('masters_and_challengers4.csv')

d = {'name': pd.concat([seedData["name"], challengerData["name"]]),
    'summonerIds': pd.concat([seedData['summonerIds'], challengerData["ids"]]),   
    'accountIds': pd.concat([seedData['accountIds'],challengerData['accountId']]),
    'totalChampScores':pd.concat([seedData["totalChampScores"],challengerData["totalChampScores"]]),
    'Champ1':pd.concat([seedData["Champ1"],challengerData["Champ1"]]),
    'Champ1Points':pd.concat([seedData["Champ1Points"],challengerData["Champ1 Points"]]),
    'Champ2':pd.concat([seedData["Champ2"],challengerData["Champ2"]]),
    'Champ2Points':pd.concat([seedData["Champ2Points"],challengerData["Champ2 Points"]]),
    'Champ3':pd.concat([seedData["Champ3"],challengerData["Champ3"]]),
    'Champ3Points':pd.concat([seedData["Champ3Points"],challengerData["Champ3 Points"]]),
    'rank':pd.concat([seedData["rank"],challengerData["rank"]])
}

df = pd.DataFrame(data=d)
ordered = df[["name","summonerIds","accountIds","totalChampScores","Champ1","Champ1Points","Champ2",
"Champ2Points","Champ3","Champ3Points","rank"]]
print(list(ordered))
ordered.to_csv('mergedData.csv')
