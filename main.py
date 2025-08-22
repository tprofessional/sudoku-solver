# referencing https://www.youtube.com/watch?v=eAFcj_2quWI&ab_channel=Insidecode for brute force solver
# this program is a sudoku solver which employs backtracking to find the solution of a partially prefilled, valid grid

from collections import defaultdict
import numpy as np

class Sudoku:
    def __init__(self):
        # 2x2 grid
        self.grid = np.array(ndmin=2)


'''
    Checks if a given cell can be assigned value n and maintain a valid board

    Args:
        r - row index
        c - col index
        n - number to input in the cell
    
    Returns:
        True if n is a valid input
        False otherwise
'''
def is_valid(grid, r, c, n):
    # get index of box row and col
    box_r = r // 3 * 3
    box_c = c // 3 * 3

    # check if n is unique in its row and col
    not_in_row = n not in grid[r]
    not_in_col = n not in [grid[i][c] for i in range(9)]

    # check if n is unique in its box
    not_in_box = n not in [grid[i][j] for i in range(box_r, box_r + 3) for j in range(box_c, box_c + 3)]

    return not_in_row and not_in_col and not_in_box

'''
    Recursive method to  fill in values of the grid until a solution is reached
    
    Args:
        grid - 2x2 grid
        r - row index
        c - col index
    
    Returns:
        
'''
def solve(grid, r=0, c=0):
    # base case and early stop conditions
    if r == 9:
        # filled every row, so a valid solution was found
        return True # maybe return grid?
    elif c == 9:
        # reached last column, so start at idx 0 of next row
        return solve(grid, r + 1, 0)
    elif grid[r][c] != 0:
        # if cell is filled alr, move on
        return solve(grid, r, c + 1)
    else:
        # iterate through all possible values of n and check if it's valid
        for n in range(1,10):
            if is_valid(r, c, n):
                # assign n to the cell
                grid[r][c] = n
                # recurse based on this state
                if solve(grid, r, c + 1):
                    return True
    return False
            
