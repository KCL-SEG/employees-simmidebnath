"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, hours, hourly_pay, contracts, commission, bonus):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourly_pay = hourly_pay
        self.contracts = contracts
        self.commission = commission
        self.bonus = bonus
        self.pay = 0

    def get_pay(self):
            return self.pay


    def __str__(self):
        output = ''
        if self.salary:
            output = self.name + " works on a monthly salary of " + str(self.salary)
        else:
            output = self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.hourly_pay) + "/hour"
        if self.contracts:
            output += " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.commission) + "/contract"
        if self.commission:
            output += " and receives a bonus commission of " + str(self.bonus)
        
        output += ". Their total pay is " + str(self.get_pay()) + "."
        return output



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
