try:
  num1=int(input("enter first number: "))
  num2=int(input("enter second number: "))

  result = num1/num2
  print("RESULT:", result)

except ZeroDivisionError as z:
  print("Common man, this is Zero Division Error")
except SyntaxError as s:
  print("Common man, this is Syntax Error")
except ValueError as v:
  print("Common man, this is Value Error")
except:
  print("Common man, some new error")
finally:
  print("this will print no matter what")
