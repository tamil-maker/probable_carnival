sortnum = []
for i in range(1,6):
    data = int(input("enter the  number:"))
    sortnum.append(data)     
print("my list:",sortnum)
l=len(sortnum)
for i in range(int(l/2)):
    temp=sortnum[i]
    sortnum[i]=sortnum[l-i-1]
    sortnum[l-i-1]=temp
    print("my sort number list is:",sortnum)

"""
def max_num(my_new_list):
    max=0
    for i in range(len(my_new_list)):
        i > max 
        max = i
        return max
max_element = max_num(my_new_list)
print (max_element)
def sort_val(my_sort):
    for i in range(len(my_sort)):
        if my_sort[i] < my_sort[j]:
            my_sort[j],my_sort[i] = my_sort[i],my_sort[j]
            return  my_sort_list  
my_sort_list = sort_val(my_sort) 
print("order is:",my_sort_list)  
"""      

