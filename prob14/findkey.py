# -*- coding: utf-8 -*-
from collections import defaultdict
import string
''' thought about using the dictionary, but it's not really needed for this problem =)
filedict = open('boozzle-dict.txt')
d_set = set([])
pref_set = set([])
for line in filedict:
  d_set.add(line[:-1])
  for i in range(1,len(line)):
    pref_set.add(line[:i])
filedict.close()
'''
#simple function to convert cipher(list of ints [0,255]) to text using a key (list of ints [0,255])
def totext(cipher, key):
  return ''.join([chr(cipher[i] ^ key[i]) for i in range(len(cipher))])
    

#accept any letter, punctuation, space, number
accept = map(ord,string.letters) + [32, 45] + range(33,45) + range(46,65)
#dictionary with scoring function for different characters
score = {}
#most of the text should be lowercase
for c in string.ascii_lowercase:
  score[ord(c)] = 10
#and space
score[ord(' ')] = 5
#a few upper case letters here and there
for c in string.ascii_uppercase:
  score[ord(c)] = 3
#punctuation and numbers should be rare
for c in range(33,65):
  score[c] = 1

ciphers = []

while True:
  try:
    #read from the file with ciphered messages (one per line) and convert hex to int
    s = raw_input()
    cipher = [int(s[2*j:2*j+2],16) for j in range(len(s)/2)]
    ciphers.append(cipher)
  except:
    break


best = []    
#run through the characters until the length of the biggest cipher
for i in range(max(map(len,ciphers))):
  charscore = defaultdict(int)
  charscore[0] = 0
  mx = 0
  #run through all possible bytes that could be the key at this position
  for k in range(256):
    #and for each cipher...
    for s in ciphers:
      #if the current position is still inside the cipher
      if i < len(s):
        #if the cipher xored with this byte is not an accepted character, go to the next byte
        if k ^ s[i] not in accept:
          break
        else:
          #update the score of this byte
          charscore[k] = charscore[k] + score[k ^ s[i]]
          if charscore[k] > charscore[mx]:
            mx = k
  
  #the 'best' key is updated with the byte that gives the highest summed score for all cipher texts
  best.append(mx)


#after looking at the output, we want to correct a few key bytes
#to ensure we get sensible text
wanted = {}
wanted[(0,0)] = 'I'
wanted[(0,25)] = 'm'
wanted[(0,67)] = 'e'
wanted[(0,85)] = 'r'
wanted[(0,134)] = 'e'
wanted[(0,153)] = 'm'
wanted[(0,157)] = ' '
wanted[(1,161)] = 'e'
wanted[(3,182)] = 'i'
wanted[(3,184)] = 'u'
wanted[(9,189)] = 'e'
wanted[(9,190)] = 's'
wanted[(9,194)] = 't'
wanted[(9,197)] = 'f'
wanted[(9,199)] = 'te'
wanted[(6,203)] = 'dn'
wanted[(6,208)] = 'even have time to dry.'

for w in wanted:
  if len(wanted[w]) > 1:
    for rep in range(len(wanted[w])):
      best[w[1]+rep] = ord(wanted[w][rep]) ^ ciphers[w[0]][w[1]+rep]
  else:
    best[w[1]] = ord(wanted[w]) ^ ciphers[w[0]][w[1]]
    

#print the plaintext to make any corrections
for c in ciphers:
  print totext(c, best)

#print the key to be used in the "main program"
print best
  