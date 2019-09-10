# http://www.51nod.com/Challenge/Problem.html#problemId=1649

data = input()
dd = data.split(" ")

village = int(dd[0])
trains = int(dd[1])

matrix = [[0] * village for i in range(village)]
for i in range(trains):
    t = input()
    tt = t.split(" ")
    matrix[int(tt[0])-1][int(tt[1])-1] = 1
    matrix[int(tt[1])-1][int(tt[0])-1] = 1

def bfs(matrix, traffic):
    queue = [0]
    book = [0] * village
    book[0] = 1

    nowptr = 0
    layertail = 0
    layer = 1
    while nowptr < village and nowptr < len(queue):
        for i in range(village):
            if i != queue[nowptr] and matrix[i][queue[nowptr]] == traffic and book[i] == 0:
                queue.append(i)
                if i == village - 1:
                    return layer
                book[i] = 1
        if nowptr == layertail:
            layer += 1
            layertail = len(queue)-1
        # print("{} {} {}".format(layer, now, layertail))
        if len(queue) == village:
            return -1
        nowptr += 1
    return -1
if village == 1:
    print(0)
else:
    bus = bfs(matrix, 0)
    train = bfs(matrix, 1)

    if bus == -1 or train == -1:
        print(-1)
    elif bus > train:
        print(bus)
    else:
        print(train)

