import re
import math
import numpy as np

lines = open("2023/06/races.txt", "r").readlines()

races = [(int(x), int(y)) for x, y in zip(re.findall(" \d+", lines[0]), re.findall(" \d+", lines[1]))]

wins = [[t*(r[0] - t)> r[1] for t in range(r[0])] for r in races]

ways = [sum(w) for w in wins]
print(np.product(ways))       
    
time = int(lines[0].split(":")[1].replace(" ", ""))        
dist = int(lines[1].split(":")[1].replace(" ", ""))

b = (-1)*time
c = dist

p1 = (-1)*b/2
p2 = math.sqrt(b**2 - 4*c)/2

r1 = p1 + p2
r2 = p1 - p2

print(r1, r2)