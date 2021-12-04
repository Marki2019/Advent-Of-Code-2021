a = open('input.txt', 'r').readlines()
b = list(map(int, a))

count = 0

for x in range(len(b) - 3):
    if b[x+3] > b[x]:
        count += 1

print(count)
