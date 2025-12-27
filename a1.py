class BusFare:
    def __init__(self,distance):
        self.distance=distance

    def calculate_fare(self):
        return self.distance*10
    
class StudentFare(BusFare):
    def calculate_fare(self):
        return super().calculate_fare()*0.5
    

class SeniorFare(BusFare):
    def calculate_fare(self):
        return super().calculate_fare()*0.7
    

distance=int(input("Enter distance:"))

print("Normal Fare:",
BusFare(distance).calculate_fare()     )
print("Student Fare:",
BusFare(distance).calculate_fare()     )
print("Senior Fare:",
BusFare(distance).calculate_fare()     )


