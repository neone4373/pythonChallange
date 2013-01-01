import httplib as h

def getting(nth):
  url = "/pc/def/linkedlist.php?nothing=" + str(nth)
  conn = h.HTTPConnection("www.pythonchallenge.com")
  conn.request("GET", url)
  r1 = conn.getresponse()
  text = r1.read()
  print text,"\n"
  next_nothing = text.split("and the next nothing is ")[1]
  #print text,next_nothing
  conn.close()
  return next_nothing

first_nothing = 12345
i = 0

Patter_change = 16044/2
next_nothing = getting(Patter_change)
while i < 200:
  #print next_nothing
  next_nothing = getting(next_nothing)
  i += 1
