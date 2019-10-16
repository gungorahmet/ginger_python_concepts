#!/usr/bin/python3
'''
INFO = There is no copy/paste information into this file.

Author:       Ahmet Gungor
Date  :       17.10.2019
Description : This code is written to understand Encapsulation concept in Python.

What is encapsulation in a nutshell?

   In Object Oriented Programming, sometimes we need to put some restrictions.
We may have some variable that we don't want to change its value but there is 
possibility that we can change into the code by mistake.

With using Encapsulation, we can prevent this risk.

Usage:

    To have a 'private' variable or a function, we need to use double 
underscores (__) such as "__pi_number" or "__welcome()".

Conclusion: Thus, we can only use these variable or functions into the class.

    IMPORTANT HINT = Actually we can reach private variables or functions 
from out of class with;
    
    {instance}._{CLASSNAME}{VARIABLENAME or FUNCTION NAME}

    But the point of encapsulation, preventing mistakes. So you already would
not run a command like that.


I will try to explain with a simple code block below.
'''

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
    
    print(calc.value)
    # Output => 5
    
    # Define "value" of  calc instance is as 10
    calc.value = 10
    
    # Print "value" of  calc instance
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
    
    
    
    