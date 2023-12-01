import numpy as np

hill_map = open('12/hills_small.txt').read().splitlines()

xys = {(i, j): hill_map[j][i] 
for i in range(len(hill_map[0])) 
for j in range(len(hill_map))}

moves = [(0,1), (1,0), (0,-1), (-1, 0)]

def possible_arcs(xy):
    steps = {}
    for m in moves:
        step = tuple(np.add(xy, m))
        if ((step not in xys.keys()) or
            (xys[step] == 'S')):
            continue
        elif (xys[step] == 'E' or
              xys[xy] == 'S' or 
              ((ord(xys[step]) - ord(xys[xy])) <= 1)):
            steps[step] = 1
    return steps

distances = {xy: possible_arcs(xy) for xy in xys if possible_arcs(xy)}

unvisited = {xy: None for xy in distances.keys()}
visited = {}

init = (0, 0)
final = (138, 20)

current = init
currentDistance = 0
unvisited[current] = currentDistance


while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)
        

        

