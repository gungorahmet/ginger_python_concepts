#!/usr/bin/python3
#
#INFO = There is no copy/paste information into this file.
#
#Author:       Ahmet Gungor
#Date  :       17.10.2019
#Description : This code is written to understand Encapsulation concept in Python.

class Calculation:

    def __init__(self):
    
        # public variable
        self.value = 5
        
        # private variable
        self.__pi_number =  3.14
        
        # Call private __welcome() function
        self.__welcome()
    
    # private function
    def __welcome(self):
        print("Welcome to the Calculation class")
    
    # public function
    def goodbye(self):
        print("See you later")
        
        
if __name__ == "__main__":
    
    calc = Calculation()
    # Output => Welcome to the Calculation class
    # Into constructor method __welcome() function is called.
    # The function is worked because it is called into its own class.
    
    print(calc.value)
    # Output => 5
    
    calc.value = 10
    
    print(calc.value)
    # Output => 10
    
    #print(calc.__pi_number)
    # Output => AttributeError: 'Calculation' object has no attribute '__pi_number'
    # Because __pi_number is a private variable.
    
    #calc.__welcome()
    # Output => AttributeError: 'Calculation' object has no attribute '__welcome'
    # Because __welcome() is a private function
    
    calc._Calculation__welcome()
    # Output => Welcome to the Calculation class
    # With this special usage, you can reach to variable or function.
    # You may have exceptional case to reach value or function somehow. 
    # That's the way. Still not recommended
    
    calc.goodbye()
    # Output => See you later
    
    
    
    