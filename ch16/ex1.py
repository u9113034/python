# ch16_1.py
def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 13:       # 如果長度不是12
        return False            # 傳回非手機號碼格式
    
    for i in range(0, 3):       # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格式
        
    if string[3] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式
   
    for i in range(4, 8):       # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格

    if string[8] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式

    for i in range(9, 13):      # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格
    return True                 # 通過以上測試

print("I love Ming-Chi: 是中國手機號碼", taiwanPhoneNum('0933-593-211'))
print("0932-999-199:    是中國手機號碼", taiwanPhoneNum('123-4999-1959'))

