viewspot=['kyoto','osaka','okinawa','taipei','taichung','vietnam','thailand','india','hongkong','china']
viewspot_sorted=[]
print('original spot:',viewspot)
viewspot.reverse()
print('reversed spot:',viewspot)
viewspot.reverse()
viewspot_sorted=sorted(viewspot)
print("小到大: ",viewspot_sorted)
viewspot_sorted=sorted(viewspot,reverse=True)
print("大到小: ",viewspot_sorted)
viewspot.insert(0,'Antarctic')
print('add first spot: ',viewspot)
viewspot.append('Arctic Sea')
print('add last spot: ',viewspot)
viewspot[int(len(viewspot)/2)]='Chicago'
print('add middle spot: ',viewspot)
del viewspot[2]
print('delete osaka: ',viewspot)
del viewspot[8]
print('delete hongkong: ',viewspot)
