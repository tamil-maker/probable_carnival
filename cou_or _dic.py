def nonrep():
    checklist=[]
    my_string={"pythonprograming"}
    for s in my_string:
        if s in my_string:
            my_string[s]+=1
        else:
            my_string=1
            checklist.appened(my_string[s]) 
    for s in checklist:
        if s==1:
            return True
        else:
            False   
result=nonrep()
print(result)                          
