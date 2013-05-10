import bisect
import heapq
import sys

N = int(raw_input())

for testcase in range(N):
  W, H, S, T = map(int,raw_input().split())
  mp = []
  for line in range(H):
    mp.append(raw_input().decode('utf-8'))
  linerocks = [[] for i in range(H)]
  colrocks = [[] for i in range(W)]
  nodes = []
  nodedict = {}
  adj_list = []
  for i in range(H):
    for j in range(W):
      if mp[i][j]=='#':
        linerocks[i].append(j)
        colrocks[j].append(i)
      else:
        nodedict[(i,j)] = len(nodes)
        nodes.append([i,j])
        adj_list.append([])
        if mp[i][j] == 'X':
          start = len(nodes)-1
        elif mp[i][j] == 'O':
          goal = len(nodes)-1
  
  
  #build adjacency list [next_node, cost]
  #where cost is an integer corresponding to
  #distance + distance covered in T seconds at speed S
  #this way, just need to divide by speed at the end
  for node in range(len(nodes)):
    y, x = nodes[node]
    next_rock_line = bisect.bisect(linerocks[y],x)
    #if there is a hole in the wall just add the goal node to the adjacency list
    if next_rock_line == len(linerocks[y]) or next_rock_line == 0:
      if next_rock_line == 0:
        adj_list[node].append((goal, S*T + x))
      else:
        adj_list[node].append((goal, S*T + W-1-x))
      continue
    else:
      stop_right = linerocks[y][next_rock_line]-1
      if stop_right != x:
        adj_list[node].append((nodedict[(y, stop_right)], S*T + stop_right - x))
      stop_left = linerocks[y][next_rock_line-1]+1
      if stop_left != x:
        adj_list[node].append((nodedict[(y, stop_left)], S*T + x - stop_left))
    
    next_rock_col = bisect.bisect(colrocks[x],y)
    #if there is a hole in the wall just add the goal node to the adjacency list
    if next_rock_col == len(colrocks[x]) or next_rock_col == 0:
      if next_rock_col == 0:
        adj_list[node].append((goal, S*T + y))
      else:
        adj_list[node].append((goal, S*T + H-1-y))
      continue
    else:
      stop_down = colrocks[x][next_rock_col]-1
      if stop_down != y:
        adj_list[node].append((nodedict[(stop_down, x)], S*T + stop_down - y))
      stop_up = colrocks[x][next_rock_col-1]+1
      if stop_up != y:
        adj_list[node].append((nodedict[(stop_up, x)], S*T + y - stop_up))
  
  #Dijkstra
  h = [(0, start)]
  visited = set()
  while True:
    cost, node = heapq.heappop(h)
    if node not in visited:
      visited.add(node)
      if node == goal:
        if (cost%S) * 2 >= S:
          print cost/S + 1
          break
        else:
          print cost/S
          break
      for next, cost_adj in adj_list[node]:
        if next not in visited:
          heapq.heappush(h, (cost + cost_adj, next))