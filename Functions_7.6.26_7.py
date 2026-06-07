try:
  number= int(input("enter the number: "))
  print("the number entered is: ",number)
except ValueError as e:
  print("somting went wrong ", e)
