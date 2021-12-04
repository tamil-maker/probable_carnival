"""
class method
"""
class Bmi_cal():
    "bmi calculator"
    def __init__(self):
        self.name=input("enter the name:")
        self.height=float(input("height:"))
        self.weight=float(input("weight:"))
        self.bmi1=self.bmi(self.weight / (self.height/100)**2)  
        return self.bmi1
"""        
    def bmi_index(self):
        if (self.bmi< 16.0):
            return "severely underweight"
        elif (self.bmi <= 18.4):
            return "underweight"
        elif (self.bmi <= 24.9):
            return "normal"
        elif (self.bmi <= 34.9):
            return "moderately obese"
        elif (self.bmi <= 39.9):
            return "severely obese"    
        else : 
            return("morbidly obese")
            """
bmi_calculator= Bmi_cal()
#bmi_calculator.bmi_index()
print(bmi_calculator)
          