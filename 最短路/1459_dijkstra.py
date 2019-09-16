# unfinished
#http://www.51nod.com/Challenge/Problem.html#problemId=1459

data = input()

dd = data.split(" ")
rooms = int(dd[0])
paths = int(dd[1])
start = int(dd[2])
end = int(dd[3])

data = input()
roomvals = data.split(" ")

matrix = [[0] * rooms for i in range(rooms)]

for i in range(paths):
    data = input()
    dd = data.split(" ")
    matrix[int(dd[0])][int(dd[1])] = int(dd[2])
    matrix[int(dd[1])][int(dd[0])] = int(dd[2])

book = [0] * rooms
book[start] = 1

dicts = [999999] * rooms

for i in range(rooms):
    if matrix[i][start] != 0 and book[i] == 0:
        dicts[i] = matrix[i][start]

first = True
score = [999999] * rooms
while True:
    ptr = -1
    min = 999999
    for i in range(rooms):
        if dicts[i] <= min and book[i] == 0:
            if dicts[i] == min and roomvals[i] < roomvals[ptr]:
                continue
            ptr = i
            min = dicts[i]
    if score[ptr] == 999999 and ptr != -1:
        score[ptr] = int(roomvals[ptr]) + int(roomvals[start])
        first = False
    if ptr == -1:
        print("{} {}".format(0, int(roomvals[ptr])), end="")
        break
    if ptr == end:
        print("{} {}".format(min, score[ptr]), end="")
        break
    book[ptr] = 1
    for i in range(rooms):
        if matrix[ptr][i] != 0 and book[i] == 0 and matrix[ptr][i] + dicts[ptr] <= dicts[i]:
            dicts[i] = matrix[ptr][i] + dicts[ptr]
            score[i] = score[ptr] + int(roomvals[i])

