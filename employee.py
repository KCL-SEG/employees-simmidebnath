"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import re 

class Employee:
    def __init__(self, name, salary, hours, hourly_pay, contracts, commission, bonus):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourly_pay = hourly_pay
        self.contracts = contracts
        self.commission = commission
        self.bonus = bonus


    def get_pay(self):
        pay = 0
        if self.salary:
            pay += self.salary
        if self.hours and self.hourly_pay:
            pay += self.hours * self.hourly_pay
        if self.contracts and self.commission:
            pay += self.contracts * self.commission
        if self.bonus:
            pay += self.bonus
        return pay


    def __str__(self):
        string = f'{self.name} works on '
        if self.salary:
            string += f'a monthly salary of {self.salary}'
        if self.hours and self.hourly_pay:
            string += f'a contract of {self.hours} hours at {self.hourly_pay}/hour'
        if self.contracts and self.commission:
            string += f' and receives a commission for {self.contracts} contract(s) at {self.commission}/contract'
        if self.bonus:
            string += f' and receives a bonus commission of {self.bonus}'
        string += f'. Their total pay is {self.get_pay()}.'
        return string

"""class HContract(Salary):
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
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)
