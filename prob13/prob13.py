# -*- coding: utf-8 -*-
from collections import defaultdict
from bisect import bisect, bisect_left

#return the number of positions in inds which are inside [beg,end]
def in_range(inds, beg, end):
  return bisect(inds, end) - bisect_left(inds, beg)

T = int(raw_input())

for testcase in range(1,T+1):
  print 'Test case #' + str(testcase)
  N, M = map(int, raw_input().split())
  arr = map(int, raw_input().split())
  #maps integers with a list of their positions in the sequence
  dic = defaultdict(list)
  for i,v in enumerate(arr):
    dic[v].append(i+1)
  #reverse sorted list of pairs (number of occurrences, integer)
  srt = sorted([(len(dic[k]), k) for k in dic], reverse=True)
  tsts = []
  for test in range(M):
    beg, end = map(int, raw_input().split())
    ivsize = end - beg + 1
    mx = 1
    st = 0
    while st < len(srt) and srt[st][0] > mx:
      lst = dic[srt[st][1]]
      ct = bisect(lst, end) - bisect_left(lst, beg)
      mx = max(ct,mx)
      st = st + 1
    print mx