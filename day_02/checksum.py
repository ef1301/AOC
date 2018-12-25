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
    for i in split:
        for j in split:
            diffs = []
            diff = 0
            for n in range(len(j)):
                if i[n] != j[n]:
                    diff += 1
                    diffs.append(i[n])
            if diff == 1:
                print(diffs)
                print(i)
                print(j)
print(common())