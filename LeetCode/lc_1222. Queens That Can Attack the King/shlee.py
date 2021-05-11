class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [[False]*8 for _ in range(8)]
        for x,y in queens:
            board[x][y] = True
        x, y = king
        answer = []
        
        for i in range(1,(x+1 if 7-x>7-y else y+1)):#좌상
            if board[x-i][y-i]:
                answer.append([x-i,y-i])
                break;
                
        for i in range(1,x+1):#상
            if board[x-i][y]:
                answer.append([x-i,y])
                break;
                
        for i in range(1,(x+1 if 7-x>y else 8-y)):#우상
            if board[x-i][y+i]:
                answer.append([x-i,y+i])
                break;
                
        for i in range(1,y+1):#좌
            if board[x][y-i]:
                answer.append([x,y-i])
                break;
                
        for i in range(1,8-y):#우
            if board[x][y+i]:
                answer.append([x,y+i])
                break;
                
        for i in range(1,(8-x if x>7-y else y+1)):#좌하
            if board[x+i][y-i]:
                answer.append([x+i,y-i])
                break;
                
        for i in range(1,8-x):#하
            if board[x+i][y]:
                answer.append([x+i,y])
                break;
        
        for i in range(1,8-(x if x>y else y)):#하우
            if board[x+i][y+i]:
                answer.append([x+i,y+i])
                break;
            
        return answer