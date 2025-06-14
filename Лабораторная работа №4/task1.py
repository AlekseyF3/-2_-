class Book:
    """
    Класс для описания книги.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта книги.
         Title: Название книги
         author: Автор книги
         pages: Количество страниц (должно быть положительным целым числом)
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def short_description(self) -> str:
        """
        Возвращает краткие характеристики книги (название, автор, кол-во страниц.
        Пример:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.short_description()
        '1984 — George Orwell, 328 стр.'
        """
        return f"{self.title} — {self.author}, {self.pages} стр."

    def add_pages(self, extra_pages: int = 10) -> None:
        """
        Увеличивает количество страниц на заданное число.
        extra_pages: Число страниц для добавления (должно быть > 0)
        ValueError: если extra_pages <= 0
        Пример:
        >>> book = Book("Sample", "Author", 100)
        >>> book.add_pages(20)
        >>> book.pages
        120
        """
        if extra_pages <= 0:
            raise ValueError("Число добавляемых страниц должно быть больше нуля.")
        self.pages += extra_pages


class CoffeeMachine:
    """
    Класс, представляющий кофемашину.
    """

    def __init__(self, model: str, water_capacity_ml: int, current_water_ml: int):
        """
         model: Название модели кофемашины
         water_capacity_ml: Максимальный объём воды в мл (> 0)
         current_water_ml: Текущий объём воды (0 <= current <= capacity)
         ValueError: при недопустимых значениях
        Пример:
        >>> cm = CoffeeMachine("Philips", 1000, 500)
        >>> cm.model
        'Philips'
        """
        if water_capacity_ml <= 0:
            raise ValueError("Ёмкость воды должна быть больше 0.")
        if not (0 <= current_water_ml <= water_capacity_ml):
            raise ValueError("Текущий объём воды должен быть от 0 до ёмкости.")
        self.model = model
        self.water_capacity_ml = water_capacity_ml
        self.current_water_ml = current_water_ml

    def brew_coffee(self, size_ml: int = 200) -> str:
        """
        Варит одну кружку кофе заданного объёма.
         Size_ml: Объём кофе в мл (по умолчанию 200 мл, должен быть > 0)
         return: Строка с сообщением об успехе
        :raises ValueError: если размер недопустим или недостаточно воды
        Пример:
        >>> cm = CoffeeMachine("Bosch", 1000, 300)
        >>> cm.brew_coffee(150)
        'Сварена кружка кофе объёмом 150 мл.'
        """
        if size_ml <= 0:
            raise ValueError("Объём кофе должен быть больше 0.")
        if size_ml > self.current_water_ml:
            raise ValueError("Недостаточно воды для варки кофе.")
        self.current_water_ml -= size_ml
        return f"Сварена кружка кофе объёмом {size_ml} мл."

    def refill(self, amount_ml: int) -> None:
        """
        Добавляет воду в кофемашину.
        amount_ml: Объём добавляемой воды (должен быть > 0)
        :raises ValueError: если amount_ml <= 0
        Пример:
        >>> cm = CoffeeMachine("Sidelong", 1000, 400)
        >>> cm.refill(300)
        >>> cm.current_water_ml
        700
        """
        if amount_ml <= 0:
            raise ValueError("Объём доливаемой воды должен быть больше 0.")
        self.current_water_ml = min(self.current_water_ml + amount_ml, self.water_capacity_ml)

    def cups_left(self, cup_size_ml: int = 200) -> int:
        """
        Возвращает количество кружек, которые можно сварить при текущем уровне воды.
        сup_size_ml: Размер одной кружки (по умолчанию 200 мл)
        return: Количество возможных кружек
        Пример:
        >>> cm = CoffeeMachine("Krupp", 1000, 800)
        >>> cm.cups_left()
        4
        """
        return self.current_water_ml // cup_size_ml


class Stack:
    """
    Класс, реализующий структуру данных стек.
    """

    def __init__(self, name: str = "DefaultStack", max_size: int = 100):
        """
    name: Имя стека
    :param max_size: Максимальное количество элементов в стеке (> 0)
    Пример:
    >>> s = Stack("MyStack", 10)
    >>> s.name
    'MyStack'
    >>> s.max_size
    10
    """
        if max_size <= 0:
            raise ValueError("Максимальный размер должен быть положительным.")
        self.name: str = name  # Атрибут 1
        self.items: list[int] = []  # Атрибут 2
        self.max_size: int = max_size  # Атрибут 3

    def push(self, item: int) -> None:
        """
    Добавляет элемент в стек.
    item: Целое число
    :raises OverflowError: если стек переполнен
    Пример:
    >>> s = Stack(max_size=1)
    >>> s.push(10)
    >>> s.items
    [10]
    """
        if len(self.items) >= self.max_size:
            raise OverflowError("Стек переполнен.")
        self.items.append(item)

    def pop(self) -> int:
        """
    Удаляет верхний элемент и возвращает его.
    :return: Верхний элемент
    :raises IndexError: если стек пуст
    Пример
    >>> s = Stack()
    >>> s.push(5)
    >>> s.pop()
    5
    """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items.pop()

    def peek(self, default: int = -1) -> int:
        """
    Возвращает верхний элемент, не удаляя его.
    default: Значение по умолчанию, если стек пуст
    :return: Верхний элемент или default
    Пример:
    >>> s = Stack()
    >>> s.peek()
    -1
    """
        return self.items[-1] if self.items else default