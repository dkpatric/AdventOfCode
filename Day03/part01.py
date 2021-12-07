import arrays

track0 = arrays.Array(12, 0)
track1 = arrays.Array(12, 0)

with open('Day03/input.txt') as file:
    for line in file:
        value = line.strip()
        for bit in range(len(track0)):
            if value[bit] == '0':
                track0[bit] += 1
            else:
                track1[bit] += 1

gamma = ''
epsilon = ''

for index in range(len(track0)):
    if track0[index] > track1[index]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
 
gamma = int(gamma, 2)
epsilon = int(epsilon, 2) 

power = gamma * epsilon

print("power consumption:", power)