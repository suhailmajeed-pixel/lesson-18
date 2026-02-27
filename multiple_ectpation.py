try:
    num1,num2 = eval(input("enter two numbers , seperated by a conna : "))
    result = num1 / num2 
    print("result is ", result )

except ZeroDivisionError :
    print("division by zero is error !!!!")

except SyntaxError :
    print("comma is missing . enter number seperate by comma like this : 1 , 2")

except:
    print("wrong input")

else:
    print("no ecptation")

finally:
    print("this will excute no matter what")