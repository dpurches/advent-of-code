import itertools

lines = open('13/pairs.txt').read().splitlines()
lines.append('')

pairs = [(eval(lines[3*i]), eval(lines[3*i + 1])) for i in range(int(len(lines)/3))]

def eval_pair(pair: tuple) -> bool:
    """Evaluate each pair of lists recursively."""
    # Convert from pair of lists to list of pairs
    items = itertools.zip_longest(*pair)

    # Iterate through each pair
    for l, r in items:
        if type(l) == int and type(r) == int:
            if l < r: return True
            if l > r: return False
            else: continue

        if type(l) == list and type(r) == list:
            if len(l) == 0 and len(r) > 0:
                return True
            if len(l) > 0 and len(r) == 0:
                return False
            evaluated = eval_pair((l, r))
            if evaluated != 'unknown':
                return evaluated
        
        # This occurs when the lengths of list differ
        # because of itertools.ziplongest
        if l == None and r != None:
            return True
        if l != None and r == None:
            return False

        if type(l) == int and type(r) != int:
            evaluated = eval_pair(([l], r))
            if evaluated != 'unknown':
                return evaluated
        if type(l) != int and type(r) == int:
            evaluated = eval_pair((l, [r]))
            if evaluated != 'unknown':
                return evaluated
    
    # return unknow if rules don't apply
    return 'unknown'

evaluations = [eval_pair(pair) for pair in pairs]

# Part 1
print("The sum of the indices of correct order pairs is",
      sum([i + 1 for i, e in enumerate(evaluations) if e]))

# Part 2

# Convert from list of pairs to list of packets and
# Add the markers
packets = list(itertools.chain(*pairs))
packets.extend(([[2]], [[6]]))

def sort_pass(packets):
    """Perform one pass of packet sorting."""
    complete = True
    for i in range(len(packets) -1):
        get = packets[i], packets[i+1]
        if not eval_pair(get):
            complete = False
            packets[i+1], packets[i] = get
    return packets, complete

complete = False
n = 0
while not complete:
    pass_list, complete = sort_pass(packets)
    n += 1

print(f"Sorting took {n} passes",
      f"The first marker is in position {[i for i, p in enumerate(pass_list) if p == [[2]]][0] +1}",
      f"The second marker is in position {[i for i, p in enumerate(pass_list) if p == [[6]]][0] +1}")


