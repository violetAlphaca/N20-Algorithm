from collections import defaultdict

n, k = map(int,input().split(" "))
link = defaultdict(list)
    
queue = [n]
newqueue = set()
for i in range(k):
    for j in range(len(queue)):
        data = queue[j]
        dataList = []
        if link[data]:
            newqueue.update(set(link[data]))
            continue
        while data>0:
            tmp = data%10
            dataList = [tmp]+dataList
            data//=10
        for x in range(len(dataList)):
            for y in range(x+1,len(dataList)):
                if x == 0 and dataList[y] == 0:
                    continue
                newData = dataList[:]
                newData[x],newData[y] = newData[y],newData[x]
                newData = int("".join(map(str,newData)))
                link[data].append(newData)
                newqueue.add(newData)
    queue = list(newqueue)
    newqueue = set()
if list(queue):
    print(max(list(queue)))
else:
    print(-1)