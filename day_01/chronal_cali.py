##PART 1
##f = open("/home/fang/AOC/day_01/input.txt")
##
##def freq():
##    start = 0
##    for item in f:
##        start = start + int(item)
##    return start

##PART 2

##def freq(dict):
##    start = 0
##    for item in f:
##        start = start + int(item)
##        dict.setdefault(start,0)
##        dict[start] += 1
##    return dict
##
##def check(dict):
##    while True:
##        for keys in dict:
##            if dict[keys] == 2:
##                return key
##            else:
##                freq(dict)


f = open("input.txt")
split = f.read().split()

def freq():
    list = []
    start = 0
    for item in split:
        start += int(item)
        list.append(start)
    return list

def check(file):
    list = []
    start = 0
    while True:
        for item in file:
            start += int(item)
            if start in list:
                return start
            else:
                list.append(start)
                
##print(freq([]))
print(check(split))

