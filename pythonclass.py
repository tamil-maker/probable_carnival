"""Exercise 1
Follow the steps:

Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__()method.
Create a variable named number_of_sides and set it equal to 3.
Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
Create a variable named my_triangle a Annapoorani Gurusamy11:08 AM
Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
Print out my_triangle.number_of_sides and print out my_triangle.check_angles()."""
class Triangle:
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    number_of_sides=3
    def check_angle(self):
        total = self.angle1 +self.angle2 +self.angle3 
        if total==180:
           return True
        else:   
           return False
my_triangle = Triangle(90,30,60)
my_triangle.check_angle()
print(my_triangle.number_of_sides,my_triangle.check_angle)       

       

    
    




