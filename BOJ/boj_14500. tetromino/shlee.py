n,m = map(int,input().split(" "))

board = []
visited = []
for i in range (n):
    board.append(list(map(int, input().split(" "))))
    visited.append([False for _ in range (m)])
    
def visit(n, x, y, visited) :
    if n == 0 : return 0
    value = board[x][y]
    visited[x][y] = True
    results = []
    if x>0 and not visited[x-1][y]:
        results.append(value+visit(n-1, x-1, y, visited))
    if y < m-1 and not visited[x][y+1]:
        results.append(value+visit(n-1, x, y+1, visited))
    if x < n-1 and not visited[x+1][y]:
        results.append(value+visit(n-1, x+1, y, visited))
    if y >0 and not visited[x][y-1]:
        results.append(value+visit(n-1, x, y-1, visited))
    visited[x][y] = False
    if results:
        return max(results)
    else:
        return 0

def visit2(x,y) :
    results = []
    if x < n-2 and y > 0:
        results.append(board[x][y] + board[x+1][y] + board[x+1][y-1] + board[x+2][y])
        
    if x < n-2 and y < m-1:
        results.append(board[x][y] + board[x+1][y] + board[x+1][y+1] + board[x+2][y])
        
    if x > 0 and y < m-2:
        results.append(board[x][y] + board[x][y+1] + board[x-1][y+1] + board[x][y+2])
        
    if x < n-1 and y < m-2:
        results.append(board[x][y] + board[x][y+1] + board[x+1][y+1] + board[x][y+2])
    if results:
        return max(results)
    else:
        return 0
    
answers = []
for i in range(n):
    for j in range(m):
        answers.append(visit(4,i,j,visited))
        answers.append(visit2(i,j))
if answers:
	print(max(answers))
else:
	print(0)