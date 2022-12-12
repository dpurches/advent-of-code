hill_map = open('12/hills.txt').read().splitlines()

xy = {(i, j): hill_map[j][i] 
for i in range(len(hill_map[0])) 
for j in range(len(hill_map))}
