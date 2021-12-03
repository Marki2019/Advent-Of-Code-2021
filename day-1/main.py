// part 1
openstuff = open('input.txt', 'r').readlines()
b = list(map(int, openstuff))

count = 0

for x in range(len(b) - 1):
    if b[x+1] > b[x]:
        count += 1

print(count)
// I'll add part 2 when I'm done with it
