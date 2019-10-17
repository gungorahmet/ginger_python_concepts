#!/usr/bin/python3
#
#INFO = There is no copy/paste information into this file.
#
#Author:       Ahmet Gungor
#Date  :       17.10.2019
#Description : This code is written to understand Abstraction concept in Python.
#
#The code should be considered about Abstraction logic rather than code design.

from abc import ABC, abstractmethod

class Device(ABC):
    
    def __init__(self):
        #Standart Tax
        self.tax = 0.03
        self.standart_tax = self.tax
    def get_total_amount(self, amount):
        self.common_tax_amount = amount + (amount * self.tax) + (amount * self.standart_tax)
        print(f"Your total payment is = {self.common_tax_amount}")
        
    @abstractmethod
    def set_device_tax(self):
        pass

# Obviously we could create a better usage for 
class Laptop(Device):
    def set_device_tax(self):
        # Laptop Tax, overrides 0.03 value
        self.tax = 0.05

class Mobile(Device):
    def set_device_tax(self):
        # Mobile Tax, overrides 0.03 value
        self.tax = 0.08


print("-"*20)

laptop = Laptop()
print(laptop.tax)
# Output => 0.03

laptop.set_device_tax()
print(laptop.tax)
# Output => 0.05

laptop.get_total_amount(1000)
# Output => 1080

print("-"*20)

mobile = Mobile()
print(mobile.tax)
# Output => 0.03

mobile.set_device_tax()
print(mobile.tax)
# Output => 0.08

mobile.get_total_amount(1000)
# Output => 1110

print("-"*20)

    
    
    
    