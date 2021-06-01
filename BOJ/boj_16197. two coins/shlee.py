n,m = map(int, input().split(" "))

board = []
x, y = (0,0)
xx,yy = (0,0)
for i in range(n):
    board.append(list(input()))
    
flag = False
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            if flag :
                x,y = i,j
            else :
                xx,yy = i,j
            flag = True
            board[i][j] = '.'
            
def move(depth,dx,dy) :
    if depth == 11:
        return 11
    global x
    global y
    global xx
    global yy
    newx = x+dx
    newy = y+dy
    newxx = xx+dx
    newyy = yy+dy
    fall = 0
    if newx == -1 or newy == -1 or newx == n or newy == m:
        fall += 1
    if newxx == -1 or newyy == -1 or newxx == n or newyy == m:
        fall += 1
    
    if fall == 1:
        return depth
    if fall == 2:
        return 11
    
    if board[newx][newy] == '#':
        newx = x
        newy = y
    if board[newxx][newyy] == '#':
        newxx = xx
        newyy = yy
    if newx == newxx and newy == newyy:
        return 11
    backx = x
    backy = y
    backxx = xx
    backyy = yy
    
    x = newx
    y = newy
    xx = newxx
    yy = newyy
    answers = []
    answers.append(move(depth+1,-1,0))
    answers.append(move(depth+1,1,0))
    answers.append(move(depth+1,0,-1))
    answers.append(move(depth+1,0,1))
    x = backx
    y = backy
    xx = backxx
    yy = backyy
    return min(answers)

answers = []
answers.append(move(1,-1,0))
answers.append(move(1,1,0))
answers.append(move(1,0,-1))
answers.append(move(1,0,1))
answer = min(answers)
if (answer == 11):
    print(-1)
else:
    print(answer)