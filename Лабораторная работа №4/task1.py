class Animal:
    """
    Базовый класс, представляющий животное.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
    """

    def __init__(self, name: str, age: int):
        self._name = name  # инкапсуляция: не предполагается прямое изменение имени
        self.age = age

    @property
    def name(self) -> str:
        """Возвращает имя животного (только для чтения)."""
        return self._name

    def speak(self) -> str:
        """Метод, который возвращает звук, издаваемый животным."""
        return "..."

    def __str__(self) -> str:
        return f"{self.__class__.__name__} по имени {self.name}, возраст {self.age}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"


class Dog(Animal):
    """
    Класс, представляющий собаку. Наследуется от Animal.

    Атрибуты:
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        """
        Возвращает звук, издаваемый собакой.
        Перегрузка метода speak() для специфичного поведения.
        """
        return "Гав!"

    def fetch(self) -> str:
        """Метод, моделирующий поведение собаки — принести палку."""
        return f"{self.name} принес(ла) палку!"

    def __str__(self) -> str:
        return f"Собака {self.name}, порода {self.breed}, возраст {self.age}"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, "
                f"breed={self.breed!r})")


class Cat(Animal):
    """
    Класс, представляющий кошку. Наследуется от Animal.

    Атрибуты:
        color (str): Цвет шерсти кошки.
    """

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def speak(self) -> str:
        """
        Перегрузка метода speak() для кошки.
        """
        return "Мяу"

    def purr(self) -> str:
        """Метод, моделирующий поведение кошки — урчание."""
        return f"{self.name} урчит."

    def __str__(self) -> str:
        return f"Кошка {self.name}, цвет {self.color}, возраст {self.age}"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, "
                f"color={self.color!r})")
