def paths(matrix):
    citys = len(matrix)
    dis = [[0] * citynum for i in range(citynum)]

    for i in range(citys):
        dis[i] = bfs(matrix, i)
    return dis

def bfs(matrix, start):
    citys = len(matrix)

    book = [0] * citys
    book[start] = 1
    queue = [start]
    dists = [0] * citys

    nowptr = 0
    layerptr = 0
    layerIdx = 1
    while nowptr < len(queue):
        for i in range(citys):
            if book[i] == 0 and matrix[queue[nowptr]][i] == 1:
                queue.append(i)
                book[i] = 1
                dists[i] = layerIdx
            if len(queue) == citys:
                return dists
        if nowptr == layerptr:
            layerptr = len(queue) - 1
            layerIdx += 1
        nowptr += 1
    return dists



data = input()
dd = data.split(" ")

citynum = int(dd[0])
sidenum = int(dd[1])

matrix = [[0] * citynum for i in range(citynum)]
for i in range(sidenum):
    side = input().split(" ")
    v = int(side[0]) - 1
    w = int(side[1]) - 1
    matrix[v][w] = 1
    matrix[w][v] = 1

condition1 = input().split(" ")
condition2 = input().split(" ")

s1, t1, l1, s2, t2, l2 = int(condition1[0]) - 1, int(condition1[1]) - 1, int(condition1[2]), int(condition2[0]) - 1,  int(condition2[1]) - 1,  int(condition2[2])

dis = paths(matrix)
print(dis)

min = 3001
if dis[s1][t1] <= l1 and dis[s2][t2] <= l2:
    min = dis[s1][t1] + dis[s2][t2]
for i in range(citynum):
    for j in range(citynum):
        if dis[s1][i] + dis[i][j] + dis[j][t1] <= l1 and dis[s2][i] + dis[i][j] + dis[j][t2] <= l2 and dis[s1][i] + dis[i][j] + dis[j][t1] + dis[s2][i] + dis[j][t2] < min:
            min = dis[s1][i] + dis[i][j] + dis[j][t1] + dis[s2][i] + dis[j][t2]
        # print("{} {} {} A".format(i, j, min))
        if dis[s1][i] + dis[i][j] + dis[j][t1] <= l1 and dis[t2][i] + dis[i][j] + dis[j][s2] <= l2 and dis[s1][i] + dis[i][j] + dis[j][t1] + dis[t2][i] + dis[j][s2] < min:
            min = dis[s1][i] + dis[i][j] + dis[j][t1] + dis[t2][i] + dis[j][s2]
            # print("{} {} {} B {} {} {} {} {}".format(i, j, min, dis[s1][i], dis[i][j], dis[j][t1], dis[t2][i], dis[j][s2]))


if min == 3001:
    print(-1)
else:
    print(sidenum - min)
