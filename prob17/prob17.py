# -*- coding: utf-8 -*-
#For each N return the sum of digits of N!
def digisum(N):
  return sum([int(c) for c in str(N)])

def fact(N):
  ret = 1
  for i in range(2,N+1):
    ret = ret * i
  return ret
  
nums = []
while True:
  try:
    n = int(raw_input())
    print digisum(fact(n))
  except:
    break