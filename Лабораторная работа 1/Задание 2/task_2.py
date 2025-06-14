from task_1 import Book, CoffeeMachine, Stack  # импорт классов из task_1.py

if __name__ == "__main__":
    # Создаем объекты с корректными аргументами
    book = Book("Война и мир", "Лев Толстой", 1200)
    coffee_machine = CoffeeMachine("DeLonghi", 1500, 1000)
    stack = Stack("МойСтек", 3)

    # Проверка методов с неправильными аргументами
    try:
        # В методе add_pages передаем отрицательное число (некорректно)
        book.add_pages(-10)
    except ValueError as e:
        print(f'Ошибка: неправильные данные')
    except TypeError as e:
        print(f'Ошибка: неправильные данные')

    try:
        # В методе brew_coffee передаем строку вместо числа
        coffee_machine.brew_coffee("большая чашка")
    except ValueError as e:
        print(f'Ошибка: неправильные данные')
    except TypeError as e:
        print(f'Ошибка: неправильные данные')

    try:
        # В метод push передаем не число, а строку
        stack.push("элемент")
    except ValueError as e:
        print(f'Ошибка: неправильные данные')
    except TypeError as e:
        print(f'Ошибка: неправильные данные')

    # Еще пример: переполнение стека
    try:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)  # должно вызвать OverflowError (если есть проверка)
    except OverflowError as e:
        print(f'Ошибка: неправильные данные')