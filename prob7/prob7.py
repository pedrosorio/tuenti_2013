# -*- coding: utf-8 -*-
filedict = open('boozzle-dict.txt')
d_set = set([])
pref_set = set([])
for line in filedict:
  d_set.add(line[:-1])
  for i in range(1,len(line)):
    pref_set.add(line[:i])
filedict.close()

di = [-1,0,1,-1,1,-1,0,1]
dj = [-1,-1,-1,0,0,1,1,1]

def dfs(i, j, word, visited, CM, WM, board, char_scores, lst):
  visited.add((i,j))
  found = {}

  if word in d_set:
    score = len(word) + sum([CM[c[0]][c[1]] * char_scores[board[c[0]][c[1]]] for c in visited]) * max([WM[c[0]][c[1]] for c in visited])
    found[word] = score
  
  for dir in range(8):
    ii = i + di[dir]
    jj = j + dj[dir]
    if ii >= 0 and ii < len(board) and jj >= 0 and jj < len(board[0]) and (ii,jj) not in visited:
      aword = word + board[ii][jj]
      if aword not in pref_set:
        continue
      fdfs = dfs(ii, jj, aword, visited, CM, WM, board, char_scores, lst + [[ii,jj]])
      for ff in fdfs:
        if ff in found:
          found[ff] = max(found[ff], fdfs[ff])
        else:
          found[ff] = fdfs[ff]
  
  visited.remove((i,j))
  return found

#return dict word -> value for all the words
#that can be obtained starting at row i column j
def find_words(i, j, CM, WM, board, char_scores):
  visited = set([])
  return dfs(i, j, board[i][j], visited, CM, WM, board, char_scores, [])
  
N = int(raw_input())
  
for testcase in range(N):
  dinput = raw_input().replace('}','')
  char_scores = dict([[cmap.split(':')[0][2], int(cmap.split(':')[1])] for cmap in dinput.split(',')])
  W = int(raw_input())
  n = int(raw_input())
  m = int(raw_input())
  board = [['A' for i in range(m)] for j in range(n)]
  CM = [[1 for i in range(m)] for j in range(n)]
  WM = [[1 for i in range(m)] for j in range(n)]
  for i in range(n):
    row = raw_input().split()
    for j in range(m):
      board[i][j] = row[j][0]
      if row[j][1] == '1':
        CM[i][j] = int(row[j][2])
      else:
        WM[i][j] = int(row[j][2])
  
  #find all possible words and corresponding values in the board
  word_dict = {}
  for i in range(n):
    for j in range(m):
      fwords = find_words(i, j, CM, WM, board, char_scores)
      for word in fwords:
        if word in word_dict:
          word_dict[word] = max(word_dict[word], fwords[word])
        else:
          word_dict[word] = fwords[word]
  
  #knapsack 0/1
  knapsack = [(value, 1+len(word)) for word,value in word_dict.iteritems()]
  dp = [0 for i in range(W+1)]
  for i in range(1,len(knapsack)+1):
    v, w = knapsack[i-1]
    for j in range(W,-1,-1):
      if j >= w:
        dp[j] = max(dp[j], dp[j-w] + v)

  print dp[W]