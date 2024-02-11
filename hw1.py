

def caching_fibonacci():
    cache = {}                                     # Створення пустого словника  

    def fibonacci(n):                              # Створення функції з можливістю кешування 
        if n <=0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:                           # Перевірка чи є вже результат для ключу 'n' у словнику cache
            return cache[n]                        # Повертає збереженний результат
            
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # Обчислення значення і присвоювання його відповідному ключу у cache
        return cache[n]                            # Повертає збереженний результат

    return fibonacci

fib = caching_fibonacci()

print(fib(15))



