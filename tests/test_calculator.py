import sys
sys.path.append("/root/Homework3/")

from calculator import Calculator
def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(3,2) == 5

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculator.subtract(3,2) == 1

def test_multiply():
    '''Test that multiplication function works '''    
    assert Calculator.multiply(3,2) == 6

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(4,2) == 2
       