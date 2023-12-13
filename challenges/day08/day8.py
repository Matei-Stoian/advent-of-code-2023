from math import lcm
from pdb import find_function


def part1():
    input = open('sample.txt').read().splitlines()
    network = dict()

    route = input[0]
    input = input[2:]

    for line in input:
        endpoint,neighbors = line.split('=')
        network[endpoint.split()[0]] = neighbors[2:-1].split(',')
        network[endpoint.split()[0]][1] = network[endpoint.split()[0]][1].strip()
    found = False
    curr = "AAA"
    ptr = 0
    ans = 0
    while found == False:
        if curr == 'ZZZ':
            found = True
            print(f'Part 1: {ans}')
        if route[ptr] == 'R':
            curr = network[curr][1]
        else:
            curr = network[curr][0]
        ptr = (ptr+1)%len(route)
        ans+=1

def part2():
    input = open('input.txt').read().splitlines()
    network = dict()

    route = input[0]
    input = input[2:]
    for line in input:
        node,childrens = line.split(" = ")
        leftc,rightc = childrens[1:-1].split(", ")
        network[node] = (leftc,rightc)
    starting_nodes = [node for node in network if node.endswith('A')]
    def find_dist(start_node):
        found = False
        curr = start_node
        ptr = 0
        ans = 0
        while found == False:
            if curr.endswith('Z'):
                found = True
            if route[ptr] == 'R':
                curr = network[curr][1]
            else:
                curr = network[curr][0]
            ptr = (ptr+1)%len(route)
            ans+=1
        return ans-1
    ans = 1
    for node in starting_nodes:
        ans = lcm(ans,find_dist(node))
    print(f'Part 2: {ans}')

#part1()
part2()