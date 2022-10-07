"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

"""class Employee:
    def __init__(self, name, pay, commission):
        self.name = name
        self.pay = pay
        self.commission = 0

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    
"""
class Salary:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def get_pay(self):
            return self.pay


    def __str__(self):
        return (f"{self.name} works on a monthly salary of {self.pay}. Their total pay is {self.pay}")


class HContract(Salary):
    def __init__(self, name, pay, hourlyRate, numHours):
        super().__init__(name, pay)
        self.hourlyRate = hourlyRate
        self.numHours = numHours
        self.commission = 0

    def get_pay(self):
        self.pay = self.hours * self.hour_rate 
        return self.pay
     
class Bonus(Salary): 
    def __init__(self, name, pay, commission):
        super().__init__(name, pay)
        self.commission = commission

"""
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

"""
