lines = [line.strip() for line in open('input.txt').readlines()]
games = [x.split(':')[1] for x in lines]

def part1():
    ans = 0
    for i in range(len(games)):
        r,g,b = [0,0,0]
        rounds = games[i].split(';')
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                number,color = cube.split()
                number = int(number)
                if color == 'blue':
                    b = max(b,number)
                elif color == 'red':
                    r = max(r,number)
                else:
                    g = max(g,number)
        if r <=12 and g<=13 and b<=14:
            ans += i+1
    print(f'Part 1: {ans}')
def part2():
    ans = 0
    for i in range(len(games)):
        r,g,b = [0,0,0]
        rounds = games[i].split(';')
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                number,color = cube.split()
                number = int(number)
                if color == 'blue':
                    b = max(b,number)
                elif color == 'red':
                    r = max(r,number)
                else:
                    g = max(g,number)
        ans += (r*b*g)
    print(f'Part 2: {ans}')
part1()  
part2()