f = open("/home/fang/AOC/day_01/input.txt")
read = f.read()
def makelist(input):
    list = ""
    for item in input:
        list = list + item
    return str(list)

s = makelist(read)

def freq(list,start):
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

print(freq(s, 0))
