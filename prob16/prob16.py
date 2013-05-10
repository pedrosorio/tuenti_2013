# -*- coding: utf-8 -*-
def numtobin(num, sz):
  ret = []
  st = 2**(sz-1)
  while st > 0:
    if st & num:
      ret.append('1')
    else:
      ret.append('0')
    st = st / 2
  return ''.join(ret)

def do_turing(tape):
  tapenums = tape.split('#')[1:-1]
  sznum = len(tapenums[0])
  lst = [int(b,2) for b in tapenums]
  return '#'+numtobin(lst[0] * sum(lst[1:]),sznum)+'#'

while True:
  try:
    tape = raw_input()
    print do_turing(tape)
  except:
    break