def height_weight():
    height = float(input("enter the height:"))
    weight = float(input("enter the weight:"))
    BMI = (weight / (height/100)**2)
    print(f"your bmi is:{BMI}")
    return BMI
#user_height,user_weight = height_weight(height,weight)
def cal_BMI(BMI):#called function
    #for x,y in height_weight():
    try : 
    BMI<-12
    break
    
""""""
    if BMI < 16.0:
        print("severely underweight")
    elif (BMI <= 18.4):
        print("underweight")
    elif (BMI <= 24.9):
        print("normal")
    elif (BMI <= 34.9):
        print("moderately obese")
    elif (BMI <= 39.9):
        print("severely obese")
    else : 
        print("morbidly obese")  
         #return(cal_BMI)""""
BMI_value = height_weight()
cal_BMI(BMI_value)
except
print(null)