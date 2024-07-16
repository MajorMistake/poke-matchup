import requests, json

entry: str = "pi"

r = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit=10000")

data = json.loads(r.text)
possible_names = [pokemon["name"] for pokemon in data["results"]]

result = [name for name in possible_names if entry.lower() in name.lower()]

print(result)