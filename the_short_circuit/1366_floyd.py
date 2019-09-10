
# http://www.51nod.com/Challenge/ProblemSubmitDetail.html
# 1
# 5 5
# NNNNY
# NNYNN
# NYNYN
# NNYNY
# YNNYN
# 只有这个没过，用了个low逼办法过了，两次floyd

count = int(input())

def circle():
    data = input()
    dd = data.split(" ")
    man = int(dd[0])
    diff = int(dd[1])

    if man == 1:
        return diff

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
    return floyd(man, diff, matrix)

def floyd(man, diff, matrix):
    for i in range(man):
        for j in range(man):
            for k in range(man):
                if (matrix[i][j] > matrix[i][k] + matrix[k][j] or matrix[i][j] == 0) and i != j and i != k and j != k and matrix[i][k] != 0 and matrix[j][k] != 0:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    matrix[j][i] = matrix[i][k] + matrix[k][j]

    # for i in range(man):
    #     for j in range(man):
    #         for k in range(man):
    #             if (matrix[i][j] > matrix[i][k] + matrix[k][j] or matrix[i][j] == 0) and i != j and i != k and j != k and matrix[i][k] != 0 and matrix[j][k] != 0:
    #                 matrix[i][j] = matrix[i][k] + matrix[k][j]
    #                 matrix[j][i] = matrix[i][k] + matrix[k][j]

    max = 0
    for i in range(man):
        for j in range(man):
            # 取最大间隔
            if matrix[i][j] > max and i != j:
                max = matrix[i][j]

    # for i in matrix:
    #     print(i)

    # 判断是否是连通图
    book = [0] * man
    dfs(man, matrix, book, 0)
    for i in range(man):
        if book[i] == 0:
            return -1
    return max * diff

def dfs(man, matrix, book, now):
    for i in range(man):
        if book[i] == 0 and matrix[i][now] != 0:
            book[i] = 1
            dfs(man, matrix, book, i)


for i in range(count):
    print(circle())
