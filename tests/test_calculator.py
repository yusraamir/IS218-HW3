'''My Calculator Test'''
import sys
sys.path.append("/root/Homework3/")
from calculator import add, subtract
def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
    
