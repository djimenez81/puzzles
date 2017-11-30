function sudoku = insertValue(sudoku,idx,val)
% This function inserts the value given into the sudoku grid, if it is possible
% to do it and retain a valid grid after it is added.
%
% INPUT :
%   - sudoku: The sudoku structure before val has been added in possition idx.
%   - idx: Index of the position where the value should be added.
%   - val: The value to be added to the grid on position idx.
%
% OUPUT :
%   - sudoku: The structure with the sudoku grid once the value has been added.
%
  sudoku.grid(idx) = val;
end
