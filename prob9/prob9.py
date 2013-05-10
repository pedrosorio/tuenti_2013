T = int(raw_input())

def turns(W,H,S,C,G,N):
  if N >= W:
    return -1
  #number of times we can use crematorium
  nfurnace = (G - S*N)/C
  #invasion after turn
  turninv = (W*H - N) / (W - N)
  
  return (nfurnace+1) * turninv

for testcase in range(T):
  W, H, S, C, G = map(int, raw_input().split())
  #compute max soldiers that can be bought
  mxs = G/S
  #solution linear in mxs
  if mxs >= W:
    print -1
  else:
    maxtime = 0
    for numsoldiers in range(mxs+1):
      maxtime = max(maxtime,turns(W,H,S,C,G,numsoldiers))
    print maxtime
