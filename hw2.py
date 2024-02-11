from typing import Callable
import re
from functools import reduce

def generator_numbers(text: str):
    numbers = map(float,filter(lambda x: re.match(r'\b\d+\.\d+\b', x), text.split(" "))) 
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
    return reduce(lambda x,y: x+y ,func(text))
    

if __name__=="__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний прибуток: {total_income}")

