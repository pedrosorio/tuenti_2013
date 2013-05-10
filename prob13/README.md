Process the array of each test case, building a hash map from each number in the array to a list of the positions it occurs in.

Create a sorted (in descending order) list of pairs (number of occurrences, number). For each query, go through this list and find how many times each number appears in the interval using binary search on the list of positions computed previously O(log M), M = number of times the number appears in the list. 

The search for the max repetitions stops when the element being checked appears the same or less times in the whole list than the maximum repeated number found so far. 

For an array of N elements where each number appears repeated M times, there are N/M different numbers. This is O(N/M * log(M)) for each query. This approach works very well if there are very few different numbers in the list, i.e. M is large. It is very poor when each number appears only once or twice in the whole list.