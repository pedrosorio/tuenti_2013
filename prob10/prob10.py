# -*- coding: utf-8 -*-
import hashlib
import bisect

#contains implicit representation of the huge string
class ImpStr:
  def __init__(self, input, si):
    self.strs = []
    self.imps = []
    self.mult = []
    self.start = si
    curstr = []
    while si < len(input):
      if input[si]=='[':
        dj = si-1
        mult = 1
        num = 0
        while dj >= 0 and input[dj] in '0123456789':
          num = mult * (ord(input[dj]) - ord('0')) + num
          mult = mult * 10
          dj = dj - 1
          curstr.pop()
        self.mult.append(num)
        self.strs.append(''.join(curstr))
        curstr = []
        newimp = ImpStr(input, si+1)
        self.imps.append(newimp)
        si = newimp.end + 1
      elif input[si]==']':
        self.strs.append(''.join(curstr))
        self.end = si - 1
        self.lens = [item for sublist in zip(map(len,self.strs), [a*b.len for a,b in zip(self.mult, self.imps)]) for item in sublist] + [len(self.strs[-1])]
        self.len = sum(self.lens)
        for i in range(2,len(self.lens)):
          self.lens[i] = self.lens[i]+self.lens[i-1]
        #for every string that is smaller than a given size, make it "compact"
        if self.len < 1e7:
          self.strs = [''.join([self.strs[i] + self.mult[i] * self.imps[i].strs[0] for i in range(len(self.imps))]) + self.strs[-1]]
          self.imps = []
          self.mult = []
          self.lens = [self.len]
        return
      else:
        curstr.append(input[si])
      si = si + 1
    self.strs.append(''.join(curstr))
    self.lens = [item for sublist in zip(map(len,self.strs), [a*b.len for a,b in zip(self.mult, self.imps)]) for item in sublist] + [len(self.strs[-1])]
    self.len = sum(self.lens)
    for i in range(2,len(self.lens)):
      self.lens[i] = self.lens[i]+self.lens[i-1]
    if self.len < 1e7:
      self.strs = [''.join([self.strs[i] + self.mult[i] * self.imps[i].strs[0] for i in range(len(self.imps))]) + self.strs[-1]]
      self.imps = []
      self.mult = []
      self.lens = [self.len]

  #fetch recursively string data with length ilen from the object, starting at istart
  #the string data is appended to the array "appendTo"
  def get(self, appendTo, istart, ilen):
    st = bisect.bisect(self.lens, istart)
    ilen = min(self.len - istart, ilen)
    if st > 0:
      istart = istart - self.lens[st-1]
      
    while ilen > 0:
      if st%2 == 0:
        glen = min(ilen, len(self.strs[st/2])-istart)
        appendTo.append(self.strs[st/2][istart:istart+glen])
        istart = 0
        ilen = ilen - glen
      else:
        simp = self.imps[st/2]
        stimp = istart/simp.len
        istart = istart%simp.len
        glen = min(ilen, simp.len-istart)
        simp.get(appendTo, istart, glen)
        ilen = ilen - glen
        istart = 0
        stimp = stimp + 1
        if ilen > 0:
          numtot = min(self.mult[st/2] - stimp, ilen/simp.len)
          if numtot > 0:
            aux = []
            simp.get(aux, 0, simp.len)
            appendTo.extend(numtot * aux)
            stimp = stimp + numtot
            ilen = ilen - numtot * simp.len
          if stimp < self.mult[st/2]:
            simp.get(appendTo, 0, ilen)
            ilen = 0
      st = st + 1
      
while True:
  try:
    input = raw_input()
  except:
    break
  megaobject = ImpStr(input,0)
  h = hashlib.md5()
  i = 0
  while i < megaobject.len:
    aux = []
    megaobject.get(aux, i, 50000000)
    h.update(''.join(aux))
    i = i + 50000000
  print h.hexdigest()