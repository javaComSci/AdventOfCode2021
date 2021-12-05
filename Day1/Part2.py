values = []
with open('data.txt') as f:
    for line in f:
        values.append(int(line))

i = 0
currSum = 0
prevSum = 0
while i < 3:
    prevSum += values[i]
    i += 1

increases = 0
while i < len(values):
    currSum = prevSum - values[i-3] + values[i]
    if currSum > prevSum:
        increases += 1
    prevSum = currSum
    i += 1

print(increases)
