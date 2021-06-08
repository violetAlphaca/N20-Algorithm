from collections import defaultdict

def dfs(x,y,step):
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    global maxStep
    maxStep = max(step, maxStep)
    for dx, dy in d:
        if x+dx < 0 or x+dx >= c or y+dy < 0 or y+dy >= r:
            continue
        nextAlphabet = board[x+dx][y+dy]
        if visited[nextAlphabet]:
            continue
        visited[nextAlphabet] = True
        dfs(x+dx,y+dy, step+1)
        visited[nextAlphabet] = False

c,r = map(int,input().split(" "))


board = []
for i in range(c):
    board.append(list(input()))

visited = defaultdict(bool)
maxStep = 1
visited[board[0][0]] = True
dfs(0,0,1)

print(maxStep)