# http://www.51nod.com/Challenge/Problem.html#problemId=1445

count = int(input())

def circle():
    man = int(input())

    matrix = [[-1] * man for i in range(man)]
    for i in range(man):
        t = input()
        j = 0
        num = 0
        for k in t:
            if k == "Y":
                matrix[i][j] = num
                num += 1
            j += 1
    print(dijkstra(man, matrix))

def dijkstra(man, matrix):
    dists = [100000] * man
    dists[0] = 0
    book = [0] * man
    book[0] = 1

    ptr = 0
    while True:
        for i in range(man):
            if matrix[ptr][i] >=0 and book[i] == 0 and dists[ptr] + matrix[ptr][i] < dists[i]:
                dists[i] = dists[ptr] + matrix[ptr][i]
        min = 100000
        f = False
        for i in range(man):
            if book[i] == 0:
                if min > dists[i]:
                    f = True
                    min = dists[i]
                    ptr = i
        if ptr == man -1:
            return dists[ptr]
        if not f:
            break
            # if max == 10000:
            #     return 0
            # return max
        book[ptr] = 1
    return -1


for i in range(count):
    circle()
