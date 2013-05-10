Knowing that the gems disappear after Z seconds, it is possible to reduce the board to a (2*Z+1) * (2*Z+1) grid.

Furthermore, all of the gems that exist at a Manhattan distance greater than Z from the starting position can be ignored (they are never reached in Z seconds).

Since searching all the possible paths in this reduced grid is still too slow, a simple heuristic is used:

* At each position (x,y) in the board, if the gems disappear after i seconds, the maximum score that can be obtained until the end is bounded above by the sum of scores of the i most valuable gems that can be found at a Manhattan distance no greater than i from (x,y).

* An approach resembling A* uses a priority queue (heap) indexed by the current score + heuristic. It is then possible to explore the most promising paths first until the most promising path has an upper bound on the score smaller or equal to the maximum score achieved. This allows the algorithm to avoid exploring most paths and guarantees optimality.