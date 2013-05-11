# -*- coding: utf-8 -*-
T = int(raw_input())

class Situation:
  def __init__(self, euros, bitcoins):
    self.euros = euros
    self.bitcoins = bitcoins
  
  #return situation with the largest amount of euros 
  #between self and other after selling coins at the current price
  def maxeuros(self, other, price):
    return Situation(max(self.euros + self.bitcoins * price, other.euros + other.bitcoins * price), 0)

  #return situation with the largest amount of bitcoins
  #between self and other after buying coins at the current price
  def maxbitcoins(self, other, price):
    selfb = self.euros/price + self.bitcoins
    otherb = other.euros/price + other.bitcoins
    selfe = self.euros % price
    othere = other.euros % price
    if selfb == otherb:
      return Situation(max(selfe, othere), selfb)
    elif selfb > otherb:
      return Situation(selfe, selfb)
    else:
      return Situation(othere, otherb)
  
for testcase in range(T):
  N = int(raw_input())
  prices = map(int, raw_input().split())

  maxe = Situation(N, 0)
  maxb = Situation(N, 0)
  
  #O(N) =)
  for i in range(len(prices)):
    maxe, maxb = maxe.maxeuros(maxb, prices[i]), maxe.maxbitcoins(maxb, prices[i])
  print maxe.euros