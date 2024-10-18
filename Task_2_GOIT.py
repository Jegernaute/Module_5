import re


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

def generator_numbers(text):
    numbers = re.findall(r'\d+\.\d+|\d+', text) 
    for number in numbers:
        yield float(number)



def sum_profit(text, func):
    total_income  = 0
    for num in func(text):
        total_income  += num    
    return total_income 

generator_numbers(text)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income }")
