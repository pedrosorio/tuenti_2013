Very ugly magic constants all over (50000 -> maximum size of the input in the problem statement), but it makes it fast.

The problem asks to find if there is some cycle that allows to increase the energy indefinitely. Since each edge multiplies the energy by a number in the range [0.8, 1.2], an easier way to look at the problem is to compute negative log energies. After going through an edge with multiplier **m**, **E_j = E_i * m_ij**; in log Energy terms: **- log(E_j) = - log(E_i) - log(m_ij)**. 

When going through a cycle, the final energy is E_f and can be obtained from the initial energy E_i by finding the product of all the multipliers in the path, **E_f = E_i * product(m_k)**. In negative log energy terms: **- log(E_f) = - log(E_i) + sum(- log(m_k))**. Hence, if we find a cycle where the product of multipliers is bigger than one (or equivalently the sum of negative log multipliers is negative), we can increase the energy indefinitely.

The reason for looking at the problem in terms of negative log multipliers, is that finding a negative cycle (sum of edge values) in a graph is a well-known problem:

1. Initialize the distances to "infinity" (or larger than the maximum sum of edges in V steps)
2. Start with a node (0 for example) at distance 0 and place it in **to_process** list
3. Repeat V times:
4. Process all edges outgoing from nodes in the **to_process** list (if there are no nodes in the list, go to 7)
5. Update the nodes whose distances are smaller than before and place them in the **process_next** list
6. Swap the **to_process** and the **process_next** arrays (O(1) since we just swap pointers), and go to 4.
7. If there are nodes in the **to_process** list, check to see if there is some node whose distance needs to be updated. If that is the case, there must be a negative cycle (after V iterations, all nodes have their distances correctly computed in a graph with no negative cycles)
8. If no negative cycle was found but there are still nodes that weren't reached (with infinity distance), pick one of them, define its distance to be 0 and place it in **to_process** list (there may be a negative cycle in another connected component). Go to 3. 


