# ex3.py F->C or C->F temperature
conv=input("Please convert method\n1.C TEMP.\n2.F TEMP.\nChoose: ")
Temp=input("Please input TEMP: ")
if conv=="1" :
    cTemp=(float(Temp)-32)*(5/9)
    print("C Temp: ", cTemp)
else :
    fTemp = float(Temp) * (9 / 5) + 32
    print("F Temp: ", fTemp)
