"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
tuple = 'apple',2.6,8.9,0,45,67,20
print(tuple)
"""
tuple_find = input("enter the letters or digit:")
l=d=0
for i in tuple_find:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1    
    else:
        pass
    print("letters:",l) 
    print("digits:",d)







