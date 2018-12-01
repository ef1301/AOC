f = open("/home/fang/AOC/day_01/input.txt")
read = f.read()
def makelist(input):
    list = ""
    for item in input:
        list = list + item
    return str(list)

s = makelist(read)

def freq(list, start):
##    start = 0
    split = list.split()
    for item in split:
        if "-" in item:
##            print(item)
            strip = item.strip("-,")
##            print(strip)
##            print(type(strip))
            num = int(strip)
            start = start - num
        else:
##            print(item)
            strip = item.strip("+,")
##            print(strip)
##            print(type(strip))
            num = int(strip)
            start = start + num
    return start

f = freq(s,0)
print(f)

def freqdict(list,start):
    results = {}
    split = list.split()
    for item in split:
        if "-" in item:
##            print(item)
            strip = item.strip("-,")
##            print(strip)
            num = int(strip)
            start = start - num
            results.setdefault(start,0)
            results[start] += 1
        else:
##            print(item)
            strip = item.strip("+,")
##            print(strip)
            num = int(strip)
            start = start + num
            results.setdefault(start,0)
            results[start] += 1
    return results

def twice(results, start):
    for item in results:
        twice = 0
        if results[item] == 2:
            twice = item
        else:
            twice(freqdict(s,freq(s,start)), start)
    return twice

print(freqdict(s, f))
print(twice(freqdict(s, f),f))

