import urllib2
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'adminsession=true'))
f = opener.open("http://silence.contest.tuenti.net")
s = f.read()
print s
