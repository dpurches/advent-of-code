import pandas as pd
import re

def create_mapper(records, map_from, map_to):
    mapper_dict = {map_from: [], map_to: []}
    for row in records:
        row = [int(r) for r in row]
        mapper_dict[map_from].append((row[1], row[1] + row[2] -1))
        mapper_dict[map_to].append((row[0], row[0] + row[2] -1))
    print(f"{map_from}-{map_to}")
    return mapper_dict

def apply_mapper(value, mapper, map_from, map_to):
    for i, m in enumerate(mapper[map_from]):
        to_list = mapper[map_to]
        if m[0] <= value <= m[1]:
            n = value - m[0]
            return to_list[i][0] + n
    return value

def apply_rev_mapper(value, mapper, map_from, map_to):
    for i, m in enumerate(mapper[map_to]):
        to_list = mapper[map_from]
        if m[0] <= value <= m[1]:
            n = value - m[0]
            return to_list[i][0] + n
    return value



with open("2023/05/seeds.txt", "r") as f:
    parts = f.read().split("\n\n")
    
seeds = [int(p) for p in parts[0].split(" ")[1:]]

mappers = {}

for part in parts[1:]:
    lines = part.split("\n")
    groups = re.search("(\w+)-to-(\w+) .*", lines[0])
    map_from = groups[1]
    map_to = groups[2]
    
    records = [l.split(" ") for l in lines[1:]]
    mappers[(map_from, map_to)] =  create_mapper(records, map_from, map_to)

locations = {}

for s in seeds:
    value = s
    for m, map in mappers.items():
        value = apply_mapper(value, map, m[0], m[1])
        print(f"{m[1]} = {value}")
    locations[s] = value
    
def in_seeds(value, pairs):
    for p in pairs:
        if p[0] <= value <= p[1]:
            return True
    return False

is_a_seed = False
count = 0
it = iter(seeds)
zipped = zip(it, it)
pairs = [(x[0], x[0] + x[1] - 1) for x in zipped]
pos_seeds = [x for p in pairs for x in p]

def apply_mapping(mappers, value, map_from, map_to):
    first_mapped = False
    for m, map in mappers.items():
        if m[0] == map_from or first_mapped:
            value=apply_mapper(value, map, m[0], m[1])
            first_mapped = True
        if m[1] == map_to:
            return apply_mapper(value, map, m[0], m[1])

def apply_rev_mapping(mappers, value, map_from, map_to):
    first_mapped = False
    for m, map in reversed(mappers.items()):
        if m[1] == map_from or first_mapped:
            value=apply_rev_mapper(value, map, m[1], m[0])
            first_mapped = True
        if m[0] == map_to:
            return apply_rev_mapper(value, map, m[1], m[0])
    
pos_seeds = []
for m, map in mappers.items():
    from_list = [x for f in map[m[0]] for x in f]
    from_list += [x - 1 for x in from_list]
    to_list = [x for f in map[m[1]] for x in f]
    to_list += [x + 1 for x in to_list]
    for val in from_list:
        new_val = apply_rev_mapping(mappers, val, m[0], "seed")
        if in_seeds(new_val, pairs):
            pos_seeds.append(new_val)
    for val in to_list:
        new_val = apply_rev_mapping(mappers, val, m[1], "seed")
        if in_seeds(new_val, pairs):
            pos_seeds.append(new_val) 

pos_locations = {}
for s in pos_seeds:
    value = s
    for m, map in mappers.items():
        value = apply_mapper(value, map, m[0], m[1])
        print(f"{m[1]} = {value}")
    pos_locations[s] = value

print(mappers)