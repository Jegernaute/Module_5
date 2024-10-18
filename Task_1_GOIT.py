def caching_fibonacci():
    dict_cash={}
    def fibonacci(n):
        if n <= 0 :
            return 0
        elif n == 1:
            return 1
        elif n in dict_cash:
            return dict_cash[n]
        dict_cash[n] = fibonacci(n-1) + fibonacci(n-2)
        return dict_cash[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(11))  # Виведе 610
