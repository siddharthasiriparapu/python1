try:
    age = int(input("Enter the age:"))
    if(age<18):
      # let's you rais a ERROR your selfe
        raise ValueError
    else:
        print("the age is valid")
        
except ValueError:
    print("The age is not valid")
