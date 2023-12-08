import itertools
import numpy as np

schematic = open("2023/03/parts.txt").readlines()

numbers = {}
symbols = {}


for y, row in enumerate(schematic):
    number_rolling = ""
    for x, item in enumerate([*row]):
        if (not item.isnumeric()) and (row[x-1].isnumeric()):
            numbers[(x-1, y)] = number_rolling
            number_rolling = ""
        if item.isnumeric():
            number_rolling += item
            continue
        if item == "." or item == "\n":
            continue
        symbols[(x, y)]= item

def is_part(xy, number):
    coverage = []
    for i in range(len(number)):
        coverage += calc_adj(tuple(np.subtract(xy, (i, 0))))
    number_adg = set(coverage)
    
    gears_set = set(list(gears.keys()))
    gears_int = gears_set.intersection(number_adg)
    
    for xy in gears_int:
        gears[xy].append(int(number))
    
    if len(number_adg.intersection(symbols_xys)) > 0:
        return True
    else:
        return False

def calc_adj(xy):
    states = list(itertools.product([-1,0,1], repeat=2))
    return [tuple(np.add(xy, state)) for state in states]
    
symbols_xys = set(symbols.keys())
parts = []
gears = {xy: [] for xy, symbol in symbols.items() if symbol == "*"}

for xy, number in numbers.items():
    if is_part(xy, number):
        parts.append(int(number))
        
        
ratios = [num[0]*num[1] for xy, num in gears.items() if len(num) == 2]
        

        


print(numbers)        
        