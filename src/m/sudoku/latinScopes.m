function theScopes = standardScopes(n)
% This is a function that generates the standard zones or scopes of a latin
% square puzzle with n x n squares.
%
% INPUT:
%   - n: The square root of the side of the sudoku puzzle.
%
% OUTPUT:
%   - theScopes: Set of Scopes.
%
  theScopes = nan(n,2*n);

  for k=1:N
    tempMat = false(n);
    tempMat(:,k) = true;
    theScopes(:,k) = find(tempMat);
  end

  for k=1:n
    tempMat = false(n);
    tempMat(k,:) = true;
    theScopes(:,n+k) = find(tempMat);
  end

end
