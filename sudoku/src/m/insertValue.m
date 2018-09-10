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
  [X,Y] = ind2sub([N,N],idx);
  currScopes = find(sudoku.scopecell(idx,:));
  K = length(currScopes);
  valscp = false(K,1);

  for k = 1:K
    scp = currScopes(k);
    valscp(k) = sudoku.fillscop(val,scp);
  end

  if sudoku.filled(idx)
    sudoku.allowed = false;
  elseif ~sudoku.possible(X,Y,val)
    sudoku.allowed = false;
  elseif any(valscp)
    sudoku.allowed = false;
  elseif sudoku.count(val) >= N
    sudoku.allowed = false;
  else
    sudoku.filled(idx) = true;
    sudoku.possible(X,Y,:) = false;
    sudoku.possible(X,Y,val) = true;
    sudoku.count(val) = sudoku.count(val) + 1;
    for k = 1:K
      scp = currScopes(k);
      sudoku.fillscop(val,scp) = true;
      thiscope = find(sudoku.scopecell(:,scp));
      thiscope = thiscope(thiscope ~= idx);
      R = length(thiscope);
      for r = 1:R
        [x,y] = ind2sub([N,N], thiscope(r));
        sudoku.possible(x,y,val) = false;
      end
    end
    indices  = find(isnan(sudoku.grid));
    R = length(indices);
    [X,Y] = ind2sub([N,N], indices);
    B = false(R,1);
    for r = 1:R
      B(r) = any(sudoku.possible(X(r),Y(r),:));
    end
    sudoku.grid(idx) = val;
    sudoku.allowed = all(B);
  end
end
