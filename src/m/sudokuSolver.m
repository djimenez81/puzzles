function sudoku = sudokuSolver(sudoku,strategy)
% This function implements different strategies for solving the grid of a
% generalized sudoku grid.
%
% INPUT:
%   - sudoku:   Initialized gred with clues
%   - strategy: The strategy to follow to solve the grid. These are:
%     * "backtracking":
%     *
%
% OUTPUT:
%   - sudoku: The solved grid (incomplete if the strategy failed)
%
  if ~exist(strategy)
    strategy = "backtracking"
  end
end
