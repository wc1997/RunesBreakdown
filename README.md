# LeagueOfLegends_Rank_Predictor

Attemp to create CSV from league of legends API containing related features needed to do prediction.

Using riotWatcher package

1 Parse API of different ranks (Bronze, Silver, Gold, Platnium, Diamond, Masters, Challenger)

2 Create CSV for multi-class classification

3 Attemp to create a model to predict players rank based on information such as 
     cs/min, kda, win percentages, which champions are played

TODO: Current complications: 
Publically accessable ranks are Master and Challengers queues. To acccess Bronze, Silver, Gold, Plat, and Diamond queues I need to grab players in each of those ranks and then collect the corresponding league IDS. 
     1. Do summoner.by_name(region, summoner_name) for selected players in each of those ranks
          ex, summoner.by_name("na1", hissolitude)          
                         {
              "profileIconId": 3186,
              "name": "HisSolitude",
              "summonerLevel": 42,
              "accountId": 33279580,
              "id": 20359886,
              "revisionDate": 1513142165000
          }
     2. Using the id we can do league.by_summoner(region,id) to get a the league the player is in, which includes data of all          players in that league. We can then grab corresponding data the same way we did for challenger and masters.
          
