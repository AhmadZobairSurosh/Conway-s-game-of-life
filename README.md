# Conway-s-game-of-life


The Game of Life is a cellular automaton devised by the british mathematician John Horton Conway in 1970.

 The simulation starts in the first time step with a specified initial state. Each cell in the game has one of two states: "Alive" or "Dead". In the Python example, these states are expressed by the numbers 0 and 1. For the next time step, the states of the cells are calculated according to the following rules:

  *  A living cell dies if it has fewer than two living neighboring cells.
  *  A living cell with two or three living neighbors lives on.
  *  A living cell with more than three living neighboring cells dies in the next time step.
  *  A dead cell is revived if it has exactly three living neighboring cells.
