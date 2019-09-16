# http://www.51nod.com/Challenge/Problem.html#problemId=1459
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

time = 200 * paths + 1
score = 0

def dfs(nextroom, t, s):
    if nextroom == end:
        global score, time
        if t < time:
            score = s
            time = t
        elif t == time and s > score:
            score = s

    for i in range(rooms):
        if book[i] == 0 and matrix[nextroom][i] != 0:
            book[i] = 1
            dfs(i, t + matrix[nextroom][i], s + int(roomvals[i]))
            book[i] = 0

dfs(start, 0, int(roomvals[start]))
print("{} {}".format(time, score), end="")
