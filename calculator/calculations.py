import sys
sys.path.append("/root/Homework3/")

from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history:List[Calculation]= []

    @classmethod
    def add_calculation(cls, calculation:Calculation):
        cls.history.append(calculation)
    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history
    @classmethod
    def clear_history(cls):
        cls.history.clear()
    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None
    @classmethod
    def find_by_operation(cls, operation_name:str) -> List[Calculation]:
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]