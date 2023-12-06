import numpy as np

rows = open("2023/02/cubes.txt", "r").readlines()

poss_ids = []

max_cubes = {"red": 12, "green": 13, "blue": 14}

def game_possible(max_cubes, data):
    for games in data:
        games = games.split(",")
        for game in games:
            number, colour = game.strip().split(" ")
            number = int(number)
            if number > max_cubes[colour]:
                return False
    return True

def game_min(rolling_cubes, data):
    for games in data:
        games = games.split(",")
        for game in games:
            number, colour = game.strip().split(" ")
            number = int(number)
            if number > rolling_cubes[colour]:
                rolling_cubes[colour] = number
    return rolling_cubes

fewest_cubes = {}

for row in rows:
    id, data = row.split(":")
    id = int(id.strip().split(" ")[1])
    data = data.split(";")
    
    rolling_cubes = {"red": 0, "green": 0, "blue": 0}
    rolling_cubes = game_min(rolling_cubes, data)
    fewest_cubes[id] = rolling_cubes
    if game_possible(max_cubes, data):
        poss_ids.append(id)

print(poss_ids)
powers = [np.prod(list(d.values())) for d in list(fewest_cubes.values())]
print(powers)