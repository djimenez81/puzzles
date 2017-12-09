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
  elseif strategy == "human"
    sudoku = myStrategy(sudoku);
  end
end



function sudoku = backtracking(sudoku)
  % This function performs the backtracking algorithm to solve a sudoku grid.
  % It attempts to progressively input possibilities on each empty cell, until
  % there is no more possibilities to try, or the grid is completely filled.
  %
  % NOTE: This algorithm tells you if there is no solution, or finds one
  %       solution. Nevertheless, if there is more than one solution, it has no
  %       manner to detect it.
  %
  % INPUT:
  %  - sudoku: The grid to be solved.
  %
  % OUTPUT:
  %  - sudoku: The solved grid, incomplete if there is no solution.
  %
  n = 0;
  k = 1;
  keepGoing = true;
  gridSize = [sudoku.size, sudoku.size];
  emptycells = find(isnan(sudoku.clues));

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
    emptycells = dasu{k}.emptycells;
    if sudo.allowed
      k = k + 1;
      emptycells(1) = [];
      if isempty(emptycells)
        % The grid is already full
        keepGoing = false;
        sudoku = sudo;
        sudoku.backtrackingscore = n;
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
end



function sudoku = myStrategy(sudoku)
  % This method tries to emulate the way I personally would attempt to solve
  % a sudoku problem. I would first figure out if there is any cell that has a
  % single possible value, and fill it in.
  fillFlag = true;
  score = 0;
  newScore = 0;
  while fillFlag
    subScore1 = 1;
    while subScore1 > 0
      newScore(1) = newScore(1) + 1;
      [sudoku, subScore1] = fillSingleOption(sudoku);
    end

    % Here the algorithm checks out if it is time to stop.
    if all(newScore == score)
      fillFlag = false;
    else
      score = newScore;
    end
  end
end



function [sudoku,score] = fillSingleOption(sudoku)
  % It fills cells that have only one possibility left that is possible to be
  % filled.
  %
  % INPUT:
  %  - sudoku: The grid structure that needs to be analized.
  %
  % OUTPUT:
  %  - sudoku: The grid once all the possible cells have been filled.
  %  - score:  The amount of cells that were filled during the run.
  %
  score = 0;
  N = sudoku.size;
  for x = 1:N
    for y = 1:N
      if ~sudoku.filled(x,y)
        val = find(sudoku.possible(x,y,:));
        if length(val) == 1
          idx = sub2ind([N,N],x,y);
          sudo = insertValue(sudoku, idx, val);
          if sudo.allowed
            sudoku = sudo;
            score = score + 1;
          end
        end
      end
    end
  end
  printf(score);
end
