horizontal = 0
vertical = 0
aim = 0

with open('data.txt') as f:
    for line in f:
        values = line.split(" ")
        direction = values[0]
        magnitude = int(values[1])
        if direction == "forward":
            horizontal += magnitude
            vertical += (aim * magnitude)
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude
    print(horizontal * vertical)