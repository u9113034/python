# ch11_14.py
def guest_info(firstname, lastname, gender, middlename=''):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = firstname + middlename + lastname + ' 先生歡迎你'
    else:
        welcome = firstname + middlename + lastname + ' 小姐歡迎妳'
    return welcome

info1 = guest_info('Michael ', 'Jordan', 'M')
info2 = guest_info('Jennifer ', 'Lawrence', 'F')
print(info1)
print(info2)



