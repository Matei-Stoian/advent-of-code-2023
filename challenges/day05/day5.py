import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

seeds = []
mapRanges = []
seedRanges = []
seeds = list(map(int,re.findall(r'[\d]+', lines[0])))
for x in range(0,len(seeds),2):
    seedRanges.append([seeds[x],seeds[x]+seeds[x+1]-1])

lines = lines[3:]


tempRange = []
for x in lines:
    
    if(re.search(r'map',x)):
        mapRanges.append(tempRange)
        tempRange = []
    else:
        if(len(x) > 0):
            tempRange.append(list(map(int,re.findall(r'[\d]+', x))))
mapRanges.append(tempRange)          

locations = []
for range in seedRanges:
            rest = [range]
            res = []

            for map in mapRanges:
                while rest:
                    curr = rest.pop()  
                    for d, s, r in map:  
                        if curr[1] < s or s + r <= curr[0]:  
                            continue
                        elif s <= curr[0] <= curr[1] < s + r: 
                            offset = curr[0] - s
                            res.append((d + offset, d + offset + curr[1] - curr[0]))
                            break
                        elif curr[0] < s <= curr[1] < s + r:  
                            offset = curr[1] - s
                            res.append((d, d + offset))
                            rest.append((curr[0], s - 1))
                            break
                        elif s <= curr[0] < s + r <= curr[1]:  
                            offset = curr[0] - s
                            res.append((d + offset, d + r - 1))
                            rest.append((s + r, curr[1]))
                            break
                        elif curr[0] < s <= s + r <= curr[1]:  
                            res.append((d, d + r - 1))
                            rest.append((curr[0], s - 1))
                            rest.append((s + r, curr[1]))
                            break
                    else:  
                        res.append(curr)
                rest = res
                res = []
            locations.extend(rest)

print(min(i[0] for i in locations))