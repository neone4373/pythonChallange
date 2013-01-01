import pickle, urllib, sys
#print pickle("pickle")



data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

a = pickle.loads(data.read()) 
for q in a:
  line = ""
  for d in q:
   line += d[0] * d[1]
  print line
#print str(a)
#sys.stdout.write(str(len(a)))
#print ""
#sys.stdout.write(a[1:6075])
#print a[1:6075]
#sys.stdout.write(pickle.loads(a))

#print data.read()

'''
with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.vvvvvvvvvvvvvvvvvvvvvv|vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    pickled_data = pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data3 = pickle.load(f)
'''
#data3 = pickle.Unpickler(data)

#print pickled_data##print data3[:200]
