file = open("input.txt").read()
split = file.split()

def double():
    count = 0
    for item in split:
        for letter in item:
            if item.count(letter) == 2:
                count += 1
                break
            else:
                continue
    return count

def triple():
    count = 0
    for item in split:
        for letter in item:
            if item.count(letter) == 3:
                count += 1
                break
            else:
                continue
    return count

print(triple()*double())

def common():
    for item in split:
        for i in split:
            diffs = []
            diff = 0
            for n in range(len(i)):
                if item[n] != i[n]:
                    diff += 1
                    diffs.append(item[n])
            if diff == 1:
                print(diffs)
                print(item)
                print(i)
print(common())