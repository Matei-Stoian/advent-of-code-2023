from string import digits
lines = [x for x in open('input.txt').read().splitlines()]

def part1():
    symbols = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}
    gears = []
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c in symbols:
                gears.append((i,j))
    def check():
        adj = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        for x,y in poz:
            for i,j in adj:
                if (x+i,y+j) in gears:
                    return int(s)
        return 0
    s=''
    poz=[]
    numbers = []
    ans = 0
    for i,line in enumerate(lines):
        if s:
            ans += check()
            numbers.append((s,list(poz)))
            s = ''
            poz = []
        for j,c in enumerate(line):
            if s and c not in digits:
                ans += check()
                numbers.append((s,list(poz)))
                s=''
                poz=[]
            if c in digits:
                s+=c
                poz.append((i,j))
    print(f'Part 1: {ans}')

def part2():
    gears = []
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c == '*':
                gears.append((i,j))

    numbers = []

    s=''
    poz=[]
    for i,line in enumerate(lines):
        if s:
            numbers.append((s,list(poz)))
            s = ''
            poz = []
        for j,c in enumerate(line):
            if s and c not in digits:
                numbers.append((s,list(poz)))
                s=''
                poz=[]
            if c in digits:
                s+=c
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
    print(f'Part 2: {ans}')
part1()
part2()