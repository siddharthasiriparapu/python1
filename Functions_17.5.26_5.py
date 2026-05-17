def reapet(a):
  a=a+1
  print(a)
  if(a < 20):
    reapet(a)
  else:
    return
reapet(0)
