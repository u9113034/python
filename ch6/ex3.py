guest=['Kevin','Marx','Eryn']
print('目前出席人員名單: ',guest)
print('請選擇新增或刪除人員\n1.新增人員\n2.刪除人員')
ans=input('請選擇: ')
if ans=='1':
    temp=input('請輸入出席者名稱:')
    guest.append(temp)
    print(guest)
elif ans=='2':
    temp=input('請輸入欲刪除人員名稱:')
    guest.remove(temp)
    print(guest)
else:
    print('輸入錯誤,離開程式')