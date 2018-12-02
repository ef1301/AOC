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
            strip = item.strip("-")
            start = start - int(strip)
            results.setdefault(start,0)
            results[start] += 1
        else:
            strip = item.strip("+")
            start = start + int(strip)
            results.setdefault(start,0)
            results[start] += 1
    return results


def check(results):
    for item in results:
        if results[item] == 2:
            return True
        else:
            return "sad"
    
f = freq(s, 0)
print(check(f))