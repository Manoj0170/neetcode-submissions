from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        dum_box = [[".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
        for i in range(0,n,3):
            for j in range(0,n,3):
                # print(i,j)
                box = [[".",".","."],[".",".","."], [".",".","."]]
                # box2 = [[".",".","."],[".",".","."], [".",".","."]]
                for k in range(i,i+3):
                    for m in range(j,j+3):
                        box[k-i][m-j]= board[k][m]
                
                       # box2[k-i][m-j]= board[m][k]
                temp = []
                for a in box:
                    for b in a:
                        temp.append(b)
                for key in Counter(temp).keys():
                    if key!="." and Counter(temp)[key]>1:
                        return False
        for i in range(n):
            for j in range(n):
                # print(board[j][i])
                dum_box[i][j] = board[j][i]
            # break
        if not self.check_valid(board) or not self.check_valid(dum_box):
            return False
        else:
            return True


    
    
    
    
    
    
    def check_valid(self,box):
        for val in box:
            for key in Counter(val).keys():
                if key!="." and Counter(val)[key]>1:
                    return False
        return True
            
      
               
      
        