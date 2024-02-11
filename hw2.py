
import re

def generator_numbers(text):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text):
    total_profit = 0
    for number in generator_numbers(text):
        total_profit += number
    return total_profit

text = "Прибуток за перший квартал склав 1000.50, за другий - 200.75, а за третій - 150.25"
total_profit = sum_profit(text)
print("Загальний прибуток:", total_profit)

