#calculator code start from  calculation function
def calculator():
    # take input from user for calculation
    
    x = float(input("Enter 1st value  "))
    operator= input("please select operater (+,-,*,/)")
    y = float(input("Enter2nd Value "))

#define operater function
    if operator =='+':
      result = X + y
    elif operator =='-':
      result = x- y
    elif operator == '*':
      result = x * y
    elif operator == '/':
      if y !=0:
        result =x / y
      else:
        print( 'Error: divisional error' )
        return None
    else:
      print('invalid input' )

result=calculator()

print(result)
