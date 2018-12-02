
f = open("/home/fang/AOC/day_01/input.txt")

def freq(dict):
    start = 0
    for item in f:
        start = start + int(item)
        dict.setdefault(start,0)
        dict[start] += 1
    return dict

def check(dict):
    while True:
        for keys in dict:
            if dict[keys] == 2:
                return key
            else:
                freq(dict)

print(freq({}))
print(check(freq({})))

