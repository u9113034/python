# ch24_12.py
from pygal.maps.world import COUNTRIES

fnObj=open('code.txt', 'w')

for countryCode in sorted(COUNTRIES.keys()):
    print("國家代碼 :", countryCode, "  國家名稱 = ", COUNTRIES[countryCode])
    fnObj.write(countryCode+ ' '+ COUNTRIES[countryCode]+ '\n')

