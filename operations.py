number1=int(input("Enter the first number"))
number2=int(input("Enter the second number")) 
 
print(number1) 
print(number2)

operation=input("what operation do you want to do?")

if operation== '+':
 print(number1 + number2) 
elif operation=='-': 
 print(number1 - number2)  
elif operation=='*':  
 print(number1 *number2)   
elif operation=='/'and number2 !=0: 
 print(number1 / number2) 
elif operation == '/' and number2 == 0:
    print("Cannot divide by zero!")
elif operation=='**':   
 print(number1 ** number2)  
elif operation=='//' and number2 !=0:   
 print(number1 // number2) 
elif operation == '//' and number2 == 0:
    print("Cannot divide by zero!")
elif operation=='%' and number2 !=0:  
 print(number1 % number2) 
elif operation == '%' and number2 == 0:
    print("Cannot divide by zero!")

else:  
    print("Invalid! Input another  operation")

