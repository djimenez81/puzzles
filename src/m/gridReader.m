function theGrid = gridReader(gridLine)
% This function takes a string that contains, in a single line, the rows of the
% grid, with the digits in the right places, and either zeros or dots, or
% anything else in the empty slots.
%
% It assumes that the string provided is of length n^2, and that the only digits
% used are 1,2,...,n. Also, assumes that n is no greater than 16.
%
% INPUT
%   - gridLine: A string of length n^2, containing only characters from
%               123456789ABCDEFG
%
% OUTPUT
%   - gridReader: A matrix, nxn, with the values in the right places, and NaNs
%                on all other positions.
%
  theLine = "123456789ABCDEFG";
  len = length(gridLine);
  n = sqrt(len);
  theGrid = nan(n);
  for k=1:len
    if ismember(gridLine(k),theLine)
      theGrid(k) = findstr(theLine,gridLine(k));
    end
  end
  theGrid = theGrid';
end
