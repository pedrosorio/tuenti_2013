The solution starts by reading the dictionary and creating a set of words and a set of prefixes of these words.

For each test case, the solution reads the board in the specified format.

Starting at each position of the board, it runs a DFS to find all the possible words of the dictionary that can be achieved from that position. The DFS only explores nodes that correspond to prefixes existing in the dictionary (speeding up the process a lot) and computes the score for each word simultaneously. Meanwhile, a dictionary is kept with all the words found and corresponding scores. If a word is found starting at two different positions, only the largest score is kept (since we can only use a word once).

Finally, we have a set of N words (we pay 1+len(word) seconds to introduce a word) and corresponding scores, and we want to find the words that can fit in W seconds with the largest total score. This is a very well known problem known as 0/1 Knapsack, which can be solved efficiently using DP in O(W*N).