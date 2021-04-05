''' Actual Question ''''

"""
Write a function that calculates a game score

INPUT: Game Board
OUTPUT: Score

Game Board - 10x10 square grid, each cell has 1 of 7 colors
Score - 3 or more adjacent (horiz or vert) of the same color, that's worth points
  3 adjacent - 30 points
  4 adjacent - 40 points
  5 adjacent - 50 points
  6 adjacent - 60 points
  
    
  i 0 1 2 3 4 5 6 7 8 9                  i.    b[i][j].                  count_x=1
  j 
  0 r r r g b g p p p p  - 30 + 40       1      b[1][j] == b[0][j] => r      2
  1  r g y b o y o o p y - 0             2      b[2] == b[1] => r            3
  2  r g b y g y b b g g - 0             3      b[3] != b[2] => g, r         0
                                         5.     b[6] == b[5] => p.           1
                                         6.     b[7] == b[6] => p            2
                                         7.     b[8] == b[7] => p.           2
                                         8.     b[9] == b[8] => p.           4
^
30

total: 30 + 40 + 30 = 100

"""


def calculate_scores(board):
    
    rows = 10
    columns = 10
    
    count_x = 1
    count_y = 1
    
    score = 0
    
    for i in range(len(1, rows)):
        
        if board[i-1] == board[i]:
            count_x+=1
        
            if count >= 3:
                score += count_x * 10        
        else:
            count_x = 1
            
        
        for j in range(1,columns):
            if board[j-1] == board[j]:
                count_y += 1
                
                if count >= 3:
                    score += count_y * 10