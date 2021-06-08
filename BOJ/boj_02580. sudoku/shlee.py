
def validCheck(x, y, n):
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
                    if validCheck(i,j,n):
                        board[i][j] = n
                        solve()
                        board[i][j] = 0
                return
    for row in board:
        print(" ".join(map(str,row)))
    


board = []
for i in range(9) :
    board.append(list(map(int,input().split(" "))))
solve()