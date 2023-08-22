import math
#add 2no
def add(x,y):
    return x+y
#substract 2 numbers
def sub(x, y):
    return x-y
#multiply 2 number
def multiply(x,y):
    return x*y
#divide 2 numbers
def divide (x ,y ):
    if y==0:
        return "Error"
    else:
        return x/y
    
def  power(x,y):
    return x**y
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))

num1=float(input("Enter First Number:"))
Operation = input("Enter operation no:(1.add +\n ,2. sub -\n ,3. multiply *\n, 4.divide /\n ,5. power ^\n,6.sin \n,7.cos \n,8.tan\n )")

num2 = None

if Operation in ['1', '2', '3', '4', '5']:
      num2 = float(input("Enter Second Number: "))
      


if Operation == '1':
   result = add(num1,num2)

elif  Operation == '2':
    result = sub(num1,num2)
elif  Operation =='3':
    result = multiply(num1,num2)
elif  Operation =='4' :
    result = divide (num1,num2)
elif  Operation == '5':
    result = pow(num1,num2)

elif Operation =='6':
            result = sin(num1)
elif Operation == '7':
            result = cos(num1)
elif Operation == '8':
            result = tan(num1)
else :
    print("Invalid operation")
    print ("calculating\n")
    
print("First no:",num1)    
print("Second no:",num2)    
print("Result:",result)    
