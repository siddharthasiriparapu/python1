import math

def hyp(s1, s2):
  #s1^2 + s2^2 = h^2
  h=(s1*s1)+(s2*s2)
  result = math.sqrt(h)
  print("the hypotenuse is:", result)

def side(h,s1):
  #a^2 = c^2-b^2
  s2=(h*h)-(s1*s1)
  result = math.sqrt(s2)
  print("the side is:", result)

choice = input("what do you want to find ?s-side or h-hypotenuse")

if choice=="s":
  s1= int(input("enter other side value:"))
  h= float(input("enter hypotenus value: "))
  side (h, s1)
elif choice =="h":
  s1=int(input("enter side 1 value: "))
  s2=int(input("enter side 2 value: "))
  hyp(s1,s2)
else:
  print(" please choose among h or s only.")
