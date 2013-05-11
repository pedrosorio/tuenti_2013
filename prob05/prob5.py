import heapq

T = int(raw_input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

'''
for each position (x,y) in an MxN board
returns a list of the sum of the values of the i most valuable gems
at a manhattan distance <= i to (x,y)
''' 
def max_heuristic(gemdict, M, N, Z):
  return [[[sum(sorted([gemdict[gem] for gem in gemdict if abs(gem[0]-x) + abs(gem[1]-y) <= dist and gem != (x,y)], reverse = True)[:dist]) for dist in range(1,Z+1)] for y in range(N)] for x in range(M)]  

for tests in range(T):
  M, N = map(int,raw_input().split(','))
  X, Y = map(int,raw_input().split(','))
  Z = int(raw_input())
  #find the "interesting" part of the board
  minx, maxx = max(X-Z, 0), min(X+Z+1, M)
  miny, maxy = max(Y-Z, 0), min(Y+Z+1, N)
  G = int(raw_input())
  gems = [map(int,gem.split(',')) for gem in raw_input().split('#')]
  #dictionary with the gem locations that are within a manhattan distance of Z
  gemdict = dict([tuple([gem[0]-minx,gem[1]-miny]), gem[2]] for gem in gems if abs(gem[0]-X) + abs(gem[1]-Y) <= Z)
  
  #transform coordinates to focus on the interesting part of the board
  X, Y = X - minx, Y - miny
  M, N = maxx - minx, maxy - miny
      
  #precompute heuristic for maximum score than can be achieved
  maxh = max_heuristic(gemdict, M, N, Z)
  lastm = -1
  gotset = set([])
  score = 0
  if (X,Y) in gemdict:
    gotset.add((X,Y))
    score = score + gemdict[(X,Y)]
  max_attained = score
  steps = 0
  max_possible = score + maxh[X][Y][Z-1] 
  #heap where each node has the following structure (- max possible score, current score, steps, picked gems set, last movement, x, y) 
  #the first is negative because a minheap is used
  h = []
  heapq.heappush(h, (-max_possible, score, steps, gotset, -1, X, Y))
  while len(h) > 0:
    max_score, score, steps, gotset, lastm, x, y = heapq.heappop(h)
    max_score = - max_score
    if max_score <= max_attained:
      break
    steps = steps + 1
    #print max_score,score,steps,gotset,lastm,x,y
    for dir in range(4):
      if lastm != -1 and dx[dir]+dx[lastm] == 0 and dy[dir]+dy[lastm] == 0:
        continue
      xx, yy = x + dx[dir], y + dy[dir] 
      if xx >= 0 and xx < M and yy >= 0 and yy < N:
        gs = gotset.copy()
        sc = score
        if (xx,yy) in gemdict and (xx,yy) not in gotset:
          gs.add((xx,yy))
          sc = sc + gemdict[(xx,yy)]
          if sc > max_attained:
            max_attained = sc
        if steps == Z:
          continue
        max_sc = sc + maxh[xx][yy][Z-steps-1]
        #using a precomputed heuristic is faster even if the heuristic is worse
        #max_sc = sc + sum(sorted([gemdict[gem] for gem in gemdict if gem not in gs and compdist(xx,yy,gem[0],gem[1],dir) <= Z-steps], reverse = True)[:Z-steps])
        if max_sc <= max_attained:
          continue
        heapq.heappush(h, (-max_sc, sc, steps, gs, dir, xx, yy))
  
  print max_attained
  
