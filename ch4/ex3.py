# ex3.py ask user to input a 3-digit integer. Cut out the last digit to zero as like 103 to 100.
x=input("Please input a 3-digit number: ")
x=int(x)/10
print("Transfer to ", int(x)*10)
