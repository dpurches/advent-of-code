lines = open('13/pairs.txt').read().splitlines()
lines.append('')

pairs = [[eval(lines[3*i]), eval(lines[3*i + 1])] for i in range(int(len(lines)/3))]

print(pairs)
