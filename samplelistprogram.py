# reverse a list in Python
list=[]
for i in range(1,7):
    my_list=int(input("enter the number:"))
    list.append(my_list)
    print("my_list:",list)
    l=len(list)
for i in range(int(l/2)):
    temp=list[i]
    list[i]=list[l-i-1]
    list[l-i-1]=temp
    print("my_new_list:",list)

