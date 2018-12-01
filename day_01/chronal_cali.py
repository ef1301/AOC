f = open("/home/fang/AOC/day_01/input.txt")
read = f.read()
def makelist(input):
    list = ""
    for item in input:
        list = list + item
    return str(list)

print(makelist(read))

def freq(list):
    start = 0
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
print(freq(makelist(read)))