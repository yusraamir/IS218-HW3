from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
    @staticmethod
    def create(a:Decimal, b:Decimal, operation:Callable[[Decimal,Decimal],Decimal]):
        return Calculation(a,b,operation)
    
    def perform(self) -> Decimal:
        return self.operation(self.a,self.b)
    
    def __repr__(self):
        return f"Calculation({self.a},{self.b},{self.operation.__name__})"
    def get_result(self):
        return self.operation(self.a, self.b)