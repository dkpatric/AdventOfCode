with open("input.txt") as file:
    prev = int(next(file))
    count = 1
    incr = 0
    for line in file:
        curr = int(line)
        count += 1
        if curr > prev:
            incr += 1
        prev = curr
    print("Read", count, "records, increases found:", incr)

