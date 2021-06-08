
mapdict = dict()
mapdict['A'] = 0
mapdict['B'] = 1
mapdict['C'] = 2
mapdict['D'] = 3
mapdict['E'] = 4
mapdict['F'] = 5
mapdict['G'] = 6
mapdict['H'] = 7
mapdict['I'] = 8


        
def validCheck(x, y, n):
    if x<0 or x>8 or y<0 or y>8:
        return False
    for e in board[x]:
        if e == n:
            return False
    for e in [ board[i][y] for i in range(9) ]:
        if e == n:
            return False
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if board[i][j] == n:
                return False
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1,10):
                    if not validCheck(i,j,n):
                        continue
                    for m in range(n+1,10):
                        if validCheck(i+1,j,n):
                            board[i][j] = n
                            board[i+1][j] = m
                            solve()
                            board[i][j] = 0
                            board[i+1][j] = 0
                        if validCheck(i,j+1,n):
                            board[i][j] = n
                            board[i][j+1] = m
                            solve()
                            board[i][j] = 0
                            board[i][j+1] = 0
                return 
    for row in board:
        print("".join(map(str,row)))
    

count = 0
while True:
	count += 1
    inputSize = int(input())
    if inputSize == 0:
        break
    dominos = [[0]*9 for _ in range(9)]
    board = [[0]*9 for _ in range(9)]
    for i in range(9):
        dominos[i][i] = 1
    for i in range(inputSize):
        u, lu, v, lv = input().split(" ")
        u = int(u)
        v = int(v)
        dominos[u-1][v-1] = 1
        dominos[v-1][u-1] = 1
        x, y = lu
        y = int(y)-1
        x = mapdict[x]
        board[x][y] = u

        x, y = lv
        y = int(y)-1
        x = mapdict[x]
        board[x][y] = v

    for i, l in enumerate(input().split(" ")):
        x, y = l
        x = mapdict[x]
        y = int(y)-1
        board[x][y] = i+1
    print("Puzzle",count)
	solve()