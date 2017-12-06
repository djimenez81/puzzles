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
    strategy = "backtracking";
  end

  if strategy == "backtracking"
    sudoku = backtracking(sudoku);
  end
end



function sudoku = backtracking(sudoku)
  % This function performs the backtracking algorithm to solve a sudoku grid.
  n = 0;
  k = 1;
  keepGoing = true;
  gridSize = [sudoku.size, sudoku.size];

  emptycells = find(~isnan(sudoku.clues));

  if isempty(emptycells)
    % The grid was already full.
    keepGoing = false;
  else
    idx = emptycells(1);
    [x,y] = ind2sub(gridSize,idx);
    choices = find(sudoku.possible(x,y,:));
    dasu{1}.sudoku = sudoku;
    dasu{1}.emptycells = emptycells;
    dasu{1}.choices = choices;
  end

  while keepGoing
    n = n+1;
    idx = dasu{k}.emptycells(1);
    val = dasu{k}.choices(1);
    sudo = insertValue(dasu{k}.sudoku, idx, val);
    emptycells = dasu{1}.emptycells;
    if sudo.allowed
      k = k + 1;
      emptycells(1) = [];
      if isempty(emptycells)
        % The grid is already full
        keepGoing = false;
      else
        idx = emptycells(1);
        [x,y] = ind2sub(gridSize,idx);
        choices = find(sudo.possible(x,y,:));
        dasu{k}.sudoku = sudo;
        dasu{k}.emptycells = emptycells;
        dasu{k}.choices = choices;
      end
    else
      dasu{k}.choices(1) = [];
      flagChoice = isempty(dasu{k}.choices);
      while flagChoice
        dasu(k) = [];
        k = k - 1;
        if k < 1
          flagChoice = false;
          keepGoing = false;
        else
          dasu{k}.choices(1) = [];
          if ~isempty(dasu{k}.choices)
            flagChoice = false;
          end
        end
      end
      if isempty(dasu)
        keepGoing = false;
        sudoku.viable = false;
      end
    end
  end
  % What should we return.
  if sudoku.viable
    sudoku = dasu{end}.sudoku;
  end
  disp(n);
end
