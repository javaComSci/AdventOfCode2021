with open('data.txt') as f:
    num_lines = 0
    first_line = True
    counts = None
    for line in f:
        values = [int(c) for c in line.strip()]
        if first_line == True:
            counts = [0] * len(values)
            first_line = False
        for i in range(len(values)):
            counts[i] += int(values[i])
        num_lines += 1
    gamma = []
    episilon = []
    for i in range(len(counts)):
        if counts[i] > num_lines - counts[i]:
            gamma.append('1')
            episilon.append('0')
        else:
            gamma.append('0')
            episilon.append('1')
    gamma = int(''.join(gamma), 2)
    episilon = int(''.join(episilon), 2)
    print(gamma * episilon)
