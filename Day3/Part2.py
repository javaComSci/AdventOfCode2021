import copy

def bitRecurse(values, bitToLook, continueMost, continueLeast):
    count = 0
    for value in values:
        count += int(value[bitToLook])
    maxbit = 0
    if count >= len(values) - count:
        maxbit = 1
    valuesToKeepMost = []
    valuesToKeepLeast = []
    # print(len(values))
    for value in values:
        if int(value[bitToLook]) == maxbit:
            valuesToKeepMost.append(value)
        else:
            valuesToKeepLeast.append(value)
    returnMost = valuesToKeepMost
    returnLeast = valuesToKeepLeast
    if continueMost == False:
        returnMost = values
    if continueLeast == False:
        returnLeast = values
    return (returnMost, returnLeast)

with open('data.txt') as f:
    num_lines = 0
    values = []
    for line in f:
        value = line.strip()
        values.append(value)
        num_lines += 1
    
    numBit = len(values[0])
    continueMost = True
    continueLeast = True
    valuesForMost = copy.copy(values)
    for i in range(numBit):
        (valuesToKeepMost, valuesToKeepLeast) = bitRecurse(valuesForMost, i, continueMost, continueLeast)
        valuesForMost = valuesToKeepMost
        if len(valuesToKeepMost) == 1:
            print(valuesForMost)
            break
    
    valuesForLeast = copy.copy(values)
    for i in range(numBit):
        (valuesToKeepMost, valuesToKeepLeast) = bitRecurse(valuesForLeast, i, continueMost, continueLeast)
        valuesForLeast = valuesToKeepLeast
        if len(valuesToKeepLeast) == 1:
            print(valuesForLeast)
            break
    
    gamma = int(''.join(valuesForLeast[0]), 2)
    episilon = int(''.join(valuesForMost[0]), 2)

    print(gamma * episilon)