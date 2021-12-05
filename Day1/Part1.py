c = 0
with open('data.txt') as f:
    beforeValue = 10000
    for line in f:
        val = int(line)
        if val > beforeValue:
            c += 1
        beforeValue = val

print(c)