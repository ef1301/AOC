def count(record):
    count = 0
    for string in record:
##        print(string)
        count += 1
    return count
file = open("input.txt").read()
split = file.split()

#doubles
def double():
    double = []
##    triple = []
    for item in split:
        for letter in item:
            if item.count(letter) == 2:
                double.append(item)
                break
##                break
##            elif item.count(letter) == 3:
##                triple.append(item)
            else:
                continue
    return double

##print(double())        
double = double()
##print(double)

###triples
def triple():
    record = []
    for item in split:
        for letter in item:
            note = []
            if item.count(letter) == 3:
                record.append(item)
                break
            else:
                continue
    return record

##print(triple())
triple = triple()
##print(triple)

###checksum
def checksum(double, triple):
    return count(double())*count(triple())

round2 = double + triple

##def check():
##    for i in list:
##        

def common(boxes):
    ref = []
    item = 1
    while item < len(boxes):
        first = boxes[item-1]
        print(first)
        next = boxes[item]
        list = []
        item += 1
        for i in range(0,26):
##            print(list)
            if first[i] == next[i]:
##                print(first[i])
##                print(next[i])
                list.append(first[i])
            else:
                continue
                
    return list
##    print(highest)
print(common(round2))