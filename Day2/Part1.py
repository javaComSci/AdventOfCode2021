horizontal = 0
vertical = 0

with open('data.txt') as f:
    for line in f:
        values = line.split(" ")
        direction = values[0]
        magnitude = int(values[1])
        if direction == "forward":
            horizontal += magnitude
        elif direction == "down":
            vertical += magnitude
        elif direction == "up":
            vertical -= magnitude
    print(horizontal * vertical)