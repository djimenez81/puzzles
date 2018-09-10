function theScopes = standardScopes(n)
% This is a function that generates the standard zones or scopes of a sudoku
% puzzle with n^2 x n^2 squares.
%
% INPUT:
%   - n: The square root of the side of the sudoku puzzle.
%
% OUTPUT:
%   - theScopes: Set of Scopes.

  N = n^2;
  theScopes = nan(N,3*N);

  for k=1:N
    tempMat = false(N);
    tempMat(:,k) = true;
    theScopes(:,k) = find(tempMat);
  end

  for k=1:N
    tempMat = false(N);
    tempMat(k,:) = true;
    theScopes(:,N+k) = find(tempMat);
  end

  for k=1:N
    tempMat = false(N);
    i = rem(k-1,n);
    j = floor((k-1)/n);
    tempMat(n*i+1:n*i+n,n*j+1:n*j+n) = true;
    theScopes(:,2*N+k) = find(tempMat);
  end

end
