import arrays

values = arrays.Array(2000)

with open("input.txt") as file:
    index = 0
    count = 0
    for line in file:
        values[index] = int(line)
        index += 1
        count += 1
    print("Read", count, "records.")

prev = values[0] + values[1] + values[2]
index = 1
incr = 0
for index in range(1, len(values)):
    curr = values[index] + values[index + 1] + values[index + 2]
    if curr > prev:
        incr += 1
    prev = curr
    print("index:", index)
    if index + 3 > len(values) - 1:
        break

print("Increased windows:", incr)


