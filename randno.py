import random
n=4
while(n>0):
    
  a=int(input("enter num"))
  num=random.randrange(0,10)
  if a==num:
      print("win")
      break
  else:
      print("lose")
