from string import digits
lines = [x for x in open('input.txt').read().splitlines()]

gears = []
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c == '*':
            gears.append((i,j))

numbers = []

k=''
poz=[]
for i,line in enumerate(lines):
    if k:
        numbers.append((k,list(poz)))
        k = ''
        poz = []
    for j,c in enumerate(line):
        if k and c not in digits:
            numbers.append((k,list(poz)))
            k=''
            poz=[]
        if c in digits:
            k+=c
            poz.append((i,j))

def calc(x,y):
    adj = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    tmp = []
    for nuber,pos in numbers:
        for i,j in adj:
            if (x+i,y+j) in pos:
                tmp.append(int(nuber))
                break
    if len(tmp) == 2:
        return tmp[0]*tmp[1]
    return 0
ans = 0
for gear in gears:
    ans += calc(gear[0],gear[1])

print(ans)

