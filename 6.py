import httplib as h

def getting(nth):
  url = "channel/" + str(nth) + ".txt"
  f = open(url, 'r')
  line = f.readline()
  g = open(url)
  h = open("comments.txt",'a')
  for l in g:
    h.write(l+"\n")
  h.write(str(g.encoding) + "\n")
  h.write(str(i) + " __\n")
  next_nothing = line.split("Next nothing is ")[1]
  #print line, next_nothing, f.readline()
  return next_nothing

first_nothing = 90052
i = 0

Pattern_change = 16044/2
next_nothing = getting(first_nothing)
while i < 1000:
  #print next_nothing
  next_nothing = getting(next_nothing)
  i += 1

