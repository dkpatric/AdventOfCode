horizontal = 0
depth = 0
aim = 0

with open("Day02/input.txt") as file:
    for line in file:
        cmd = line.split()
        command = cmd[0]
        value = int(cmd[1])
        if command == 'forward':
            horizontal += value
            depth += value * aim
        elif command == 'down':
            aim += value
        else:
            aim -= value

print("horizontal:", horizontal, " - depth:", depth)
print("factor:", horizontal * depth)

