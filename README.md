# sudoku-solver
## Building a sudoku solver using backtracking

As an avid sudoku player, I thought it would be fun to make a sudoku solver to explore how to algorithmically approach solving puzzles.
The plan is to first implement a brute force method, then apply alpha-beta pruning for better efficiency, and then see if there are smarter ways to solve.

Dev notes:

given a puzzle, run an algorithm that solves the puzzle

recursive algorithm that solves each cell
make a choice
check constraints
update goal


9x9 board
3 subgrid

make choices and find a globally correct answer (where recursion comes in handy)
look at both approaches, brute force and backtracking

brute force: generate every single possible board of sudoku, validate each board, return valid board = exponential number of boards

whenver we see a prefilled cell, cant do anyhting
when we see an empty cell, we do a recursive call to place 1-9
we will traverse row by row (solve col 0 all the way to col 8 then reset)

constraints: placements cannot break the board

goal reached: fill the whole board (validly), or when u finish the last row and go to the next row = out of bounds