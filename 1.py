'''k = m
o = q
e = g'''
org_txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

stg = "map"

stb = "start \n" 

ll = len(stg)
i = 0
while i < ll:
  if stg[i] == "k":
    stb = stb + "m"
  elif stg[i] == "o":
    stb = stb + "q"
  elif stg[i] == "e":
    stb = stb + "g"
  elif stg[i] == "g":
    stb = stb + "i"
  elif stg[i] == "i":
    stb = stb + "k"
  elif stg[i] == "q":
    stb = stb + "s"
  elif stg[i] == "r":
    stb = stb + "t"
  elif stg[i] == "l":
    stb = stb + "n"
  elif stg[i] == "p":
    stb = stb + "r"
  elif stg[i] == "y":
    stb = stb + "a"
  elif stg[i] == "c":
    stb = stb + "e"
  elif stg[i] == "s":
    stb = stb + "u"
  elif stg[i] == "a":
    stb = stb + "c"
  elif stg[i] == "m":
    stb = stb + "o"
  elif stg[i] == "b":
    stb = stb + "d"
  elif stg[i] == "f":
    stb = stb + "h"
  elif stg[i] == "n":
    stb = stb + "p"
  elif stg[i] == "w":
    stb = stb + "y"
  elif stg[i] == "j":
    stb = stb + "l"
  elif stg[i] == "z":
    stb = stb + "b"
  elif stg[i] == "u":
    stb = stb + "w"
  elif stg[i] == "d":
    stb = stb + "f"
  elif stg[i] == "v":
    stb = stb + "x"
  elif stg[i] in [" ",".","(",")",",","'"]:
    stb = stb  +stg[i]   
  else:
    stb = stb + "_" 
    #stg[i]
  i+=1

print stg + "\n\n" + stb
