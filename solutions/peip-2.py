fn = input("Enter filename: ")
inf = open(fn, 'r')

r, c = map(int, inf.readline().strip().split(' '))

grid = []
for i in range(r):
    values = list(map(int, inf.readline().strip().split(' ')))
    grid.append(values)

n = int(inf.readline().strip())
for i in range(n):
    x1, y1, x2, y2 = map(int, inf.readline().strip().split(' '))
    sum = 0
    for j in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            sum += grid[j][k]
    print(sum)
