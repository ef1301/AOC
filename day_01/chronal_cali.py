f = open("/home/fang/AOC/day_01/input.txt")

def freq(dict):
    start = 0
    for item in f:
        start = start + int(item)
        dict.setdefault(start,0)
        dict[start] += 1
        while True:
            if dict[start] == 2:
                return start
            else:
                freq(dict)
    return dict

##def check(dict):
##    while True:
##        if dict[key] == 2:
##            return key
##        else:
##            freq(dict)

print(freq({}))
##print(check(freq({})))