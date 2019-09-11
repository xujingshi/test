# http://www.51nod.com/Challenge/Problem.html#problemId=1445
# 这种写法并不能ac！

count = int(input())

def circle():
    man = int(input())

    matrix = [[0] * man for i in range(man)]
    for i in range(man):
        t = input()
        j = 0
        for k in t:
            if k == "N":
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
            j += 1

    prefs = bfs(man, matrix)
    if prefs == None:
        print(-1)
    else:
        print(cut(prefs, matrix))

def bfs(man, matrix):
    queue = [0]
    now = 0
    nowptr = 0
    layertail = 0
    book = [0] * man
    book[0] = 1
    prefs = [-1] * man

    pre_len = 1
    while True:
        for i in range(man):
            if matrix[now][i] == 1 and book[i] == 0:
                queue.append(i)
                book[i] = 1
                prefs[i] = now
                if i == man - 1:
                    return prefs
        if nowptr == layertail:
            if pre_len == len(queue):
                return
            pre_len = len(queue)
            layertail = len(queue) - 1
        nowptr += 1
        # print("{} {} {} {}".format(now, nowptr, layertail, pre_len))
        now = queue[nowptr]

def cut(prefs, matrix):
    now = len(matrix) - 1
    num = 0
    print(prefs)
    while True:
        pref = prefs[now]
        print("当前 {} {} = {}".format(pref, now, matrix[pref][now]))
        for j in range(now):
            if matrix[pref][j] == 1:
                print("{} {} = {}".format(pref, j, matrix[pref][j]))
                num += 1
        if pref == 0:
            break
        now = pref
    return num

for i in range(count):
    circle()
