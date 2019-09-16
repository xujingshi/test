def regulate(book, i, j):
    if book[i] == -1 and book[j] != -1:
        book[i] = book[j]
    elif book[j] == -1 and book[i] != -1:
        book[j] = book[i]
    elif book[j] == -1 and book[i] == -1:
        book[i] = j
    else:
        iroot = root(book, i)
        jroot = root(book, j)
        book[iroot] = jroot
        # print("A book[{}] = {}".format(iroot, jroot))

def root(book, i):
    while True:
        newi = book[i]
        if newi == -1:
            return i
        i = newi

def sort(v, w, x):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                w[j], w[j + 1] = w[j + 1], w[j]
                x[j], x[j + 1] = x[j + 1], x[j]
    return v, w, x

def quick_sort(left, right):
    global v, w, x
    if left <= right:
        key = x[left]
        kw = w[left]
        kv = v[left]
        i = left
        j = right
        while i < j:
            while i < j and key <= x[j]:
                j -= 1
            x[i] = x[j]
            w[i] = w[j]
            v[i] = v[j]
            while i < j and x[i] <= key:
                i += 1
            x[j] = x[i]
            w[j] = w[i]
            v[j] = v[i]
        x[i] = key
        w[i] = kw
        v[i] = kv
        quick_sort(left, i - 1)
        quick_sort(i + 1, right)


d = input()
dd = d.split(" ")
nodes = int(dd[0])
sides = int(dd[1])

v, w, x = [], [], []
flags = [[0] * nodes for i in range(nodes)]
for i in range(sides):
    a = input()
    aa = a.split(" ")
    v.append(int(aa[0])-1)
    w.append(int(aa[1])-1)
    x.append(int(aa[2]))


quick_sort(0, len(x) - 1)

total = 0
count = 0
book = [-1] * nodes
nowptr = 0

while nowptr < len(v):
    start, end = 0, 0

    rootv, rootw = root(book, v[nowptr]), root(book, w[nowptr])
    if rootv != rootw:
    # if rootv != rootw or (rootv == rootw and rootv == -1):
        flags[v[nowptr]][w[nowptr]] = 1
        flags[w[nowptr]][v[nowptr]] = 1
        regulate(book, w[nowptr], v[nowptr])
        total += x[nowptr]
    nowptr += 1
print(total)
