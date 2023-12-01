import re

rows = open('2023/01/trebuchet.txt', 'r').readlines()

str_to_int = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

sums = []
p = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
for row in rows:
    digs = [x for _, x in sorted([(d.start(), d.group(1)) for d in p.finditer(row)])]
    digs = [str_to_int[d] if len(d) > 1 else d for d in digs]
    print(int(digs[0] + digs[-1]))
    if len(digs) >= 1:
        sums.append(int(digs[0] + digs[-1]))
    else:
        sums.append(0)
        
print(sums)
