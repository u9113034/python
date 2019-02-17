x=input("Please input a number: ")
try :
    print("the invert of input is ",int(x)*(-1))
except ValueError as e:
    print("not a number!")