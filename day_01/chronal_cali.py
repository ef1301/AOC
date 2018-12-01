f = open("/home/fang/AOC/day_01/input.txt")
read = f.read()
def makelist(input):
    list = ""
    for item in input:
        list = list + item
    return str(list)

print(makelist(read))

##def freq(list):
##    start = 0
##    split = list.split()
##    for item in split:
##        if "-" in item:
####            print(item)
##            strip = item.strip("-,")
####            print(strip)
####            print(type(strip))
##            num = int(strip)
##            start = start - num
##        else:
####            print(item)
##            strip = item.strip("+,")
####            print(strip)
####            print(type(strip))
##            num = int(strip)
##            start = start + num
##    return start
##print(freq(makelist(read)))

def freq(list):
    start = 0
    results = {}
    split = list.split()
    for item in split:
        if "-" in item:
##            print(item)
            strip = item.strip("-,")
##            print(strip)
##            print(type(strip))
            num = int(strip)
            start = start - num
            results.setdefault(start,0)
            results[start] += 1
        else:
##            print(item)
            strip = item.strip("+,")
##            print(strip)
##            print(type(strip))
            num = int(strip)
            start = start + num
            results.setdefault(start,0)
            results[start] += 1
    return results

def twice(dict):
    for item in dict:
        if dict[item] == 2:
            twice = item
            return twice
print(freq(makelist(read)))
print(twice(freq(makelist(read))))

