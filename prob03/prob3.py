# -*- coding: utf-8 -*-
N = int(raw_input())

def check(position, conditions):
  interval = [-1e12, 1e12]
  for cond in conditions:
    if cond[0] == 1:
      if cond[1] >= interval[1]:
	return -1
      else:
	interval = [cond[1], interval[1]]
    else:
      if cond[1] <= interval[0]:
	return -1
      else:
	interval = [interval[0], cond[1]]
  if position != -1:
    if position > interval[0] and position < interval[1]:
      return position
    else:
      return -1
  return interval

def overlaps(points, intervals):
  mx = max(points)
  mn = min(points)
  ctmn = len([iv for iv in intervals if iv[0] < mn])
  ctmx = len([iv for iv in intervals if iv[1] > mx])
  if ctmn > 1 or ctmx > 1:
    return -1
  
  ovlp = False
  # O(n^2)... so lazy =(
  for ia in range(len(intervals)):
    a = intervals[ia]
    for p in points:
      if p > a[0] and p < a[1]:
	ovlp = True
	break
    if ovlp:
      break
    for ib in range(ia+1, len(intervals)):
      b = intervals[ib]
      if min(a[1],b[1]) - max(a[0],b[0]) > 0:
	ovlp = True
	break
      if ovlp:
	break
  return ovlp
   
for sc in range(N):
  scenes = {}
  scene_names = []
  conditions = []
  position = []
  script = raw_input()
  
  cur = 0
  oriscene = -1
  prevscene = -1
  prevsymb = '.'
  invalid = False
  while cur < len(script):
    st = cur + 1
    cur = cur + 1
    while cur < len(script) and script[cur] not in '.<>':
      cur = cur + 1
    scene = script[st:cur]
    if scene not in scenes:
      curscene = len(scenes)
      scene_names.append(scene)
      scenes[scene] = len(scenes)
      conditions.append([])
      position.append(-1)
    else:
      curscene = scenes[scene]
    
    if prevscene != -1:
      if prevsymb == '<':
	conditions[curscene].append([-1, position[oriscene]])
      elif prevsymb == '>':
	conditions[curscene].append([1, position[oriscene]])
      else:
	if position[curscene] != -1 and position[curscene] != position[oriscene] + 1:
	  invalid = True
	  cur = len(script)
	else:
	  position[curscene] = position[oriscene]+1
    else:
      position[0] = 0
      
    if prevsymb == '.':
      oriscene = curscene
    
    prevscene = curscene
    if cur < len(script):
      prevsymb = script[cur]
  
  if invalid == True:
    print 'invalid'
    continue
  
  intervals = []
  points = []
  dic = {}
  for i in range(len(scenes)):
    c = check(position[i], conditions[i])
    if c == -1:
      invalid = True
      break
    if type(c) == list:
      intervals.append(c)
      dic[tuple(c)] = scene_names[i]
    else:
      points.append(c)
      dic[(c,c)] = scene_names[i]
  
  if invalid:
    print 'invalid'
    continue
  
  res = overlaps(points, intervals)
  
  if res == -1:
    print 'invalid'
    continue
  
  if res:
    print 'valid'
    continue
  
  intervals = sorted(map(tuple,intervals) + [(p,p) for p in points])
  
  print ','.join([dic[iv] for iv in intervals])