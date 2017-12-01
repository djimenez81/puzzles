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
  N = sudoku.size;
  [X,Y] = ind2sub([9,9],idx);
  currScopes = find(sudoku.scopecell(idx,:));
  K = length(currScopes);
  valscp = false(K,1);

  for k = 1:K
    scp = currScopes(k);
    valscp(k) = sudoku.fillscop(val,scp);
  end

  if sudoku.filled(idx)
    sudoku.viable = false;
  elseif ~sudoku.possible(X,Y,val)
    sudoku.viable = false;
  elseif any(valscp)
    sudoku.viable = false;
  else
    sudoku.filled(idx) = true;
    sudoku.possible(X,Y,:) = false;
    sudoku.possible(X,Y,val) = true;
    for k = 1:K
      scp = currScopes(k);
      sudoku.fillscop(val,scp) = true;
      thiscope = find(sudoku.scopecell(:,scp));
      thiscope = thiscope(thiscope ~= idx);
      R = length(thiscope);
      for r = 1:R
        [x,y] = ind2sub([9,9], thiscope(r))
        sudoku.possible(x,y,val) = false;
      end
    end
    sudoku.grid(idx) = val;
  end
end
