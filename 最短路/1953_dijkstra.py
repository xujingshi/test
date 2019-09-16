# http://www.51nod.com/Challenge/Problem.html#problemId=1953

pc = int(input())
matrix = [[0] * pc for i in range(pc)]

for i in range(pc - 1):
    data = input()
    dd = data.split(" ")
    for j in range(len(dd)):
        if dd[j] == 'x':
            matrix[i + 1][j] = 10000
            matrix[j][i + 1] = 10000
            continue
        matrix[i + 1][j] = int(dd[j])
        matrix[j][i + 1] = int(dd[j])


def dijkstra(pc, matrix):
    dists = [10000] * pc
    dists[0] = 0
    book = [0] * pc
    book[0] = 1

    max = 10000
    ptr = 0
    while True:
        for i in range(pc):
            if matrix[i][ptr] >=0 and book[i] == 0 and dists[ptr] + matrix[i][ptr] < dists[i]:
                dists[i] = dists[ptr] + matrix[i][ptr]
        min = 101
        f = False
        for i in range(pc):
            if book[i] == 0:
                f = True
                if min > dists[i]:
                    min = dists[i]
                    ptr = i
        if not f:
            if max == 10000:
                return 0
            return max
        book[ptr] = 1
        max = dists[ptr]

print(dijkstra(pc, matrix), end="")
