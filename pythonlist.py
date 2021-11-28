list = []
list.append(10)
print(list)
list1 = [10]
list1.append(20) 
print(list1)
list2 = ['apple']
list2 = list + list1 +list2
list2.append('banana')
print(list2)
list3 = []
list3 = list + list1 + list2 + list3
list3.append('grapes')
print(list3)