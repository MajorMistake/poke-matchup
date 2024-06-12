import requests, json

name = "charizard"
pokemon = {}
r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
pokeRaw = json.loads(r.text)

#pokeTypes = pokeRaw["types"]
#print("types: ", pokeTypes)

pokeStats = pokeRaw["stats"] 
stats = [] 
for item in pokeStats: 
    statObj = {} 
    statObj["name"] = item["stat"]["name"] 
    statObj["value"] = item["base_stat"] 
    stats.append(statObj) 
pokemon["stats"] = stats 
print(stats)

#pokeAbilities = pokeRaw["abilities"] 
#print("abilities: ", pokeAbilities)

#pokeMoves = pokeRaw["moves"] 
#print("moves: ", pokeMoves)