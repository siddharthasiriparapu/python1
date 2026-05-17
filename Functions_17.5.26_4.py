def sum(NUM1,NUM2):
  print("Your sum is ",NUM1 + NUM2)
def multiply(NUM1,NUM2):
  print("Your multiplied number is ",NUM1 * NUM2)
def division(NUM1,NUM2):
  print("Your divied number is ",NUM1 / NUM2)
def subtract(NUM1,NUM2):
  print("Your subtracted number is ",NUM1 - NUM2)
NUM1=int(input("Enter your first number: "))
NUM2=int(input("Enter your second number: "))
op=input("enter your operation from +,-,/,*: ")
if op=="+":
  sum(NUM1,NUM2)
elif op=="-":
  subtract(NUM1,NUM2)
elif op=="/":
  division(NUM1,NUM2)
elif op=="*":
  multiply(NUM1,NUM2)
else:
  print("Please enter a correct operator!!!")
