class Spacecraft:
    """
    Класс, описывающий космические корабли.

    Атрибуты:
        name (str): Название аппарата.
        launch_year (int): Год запуска.
    """

    def __init__(self, name: str, launch_year: int):
        self._name = name
        self.launch_year = launch_year

    @property
    def name(self) -> str:
        """Название аппарата"""
        return self._name

    def mission_info(self) -> str:
        """Информация о дате запуска аппарата"""
        return f"Аппарат {self.name}, запущен в {self.launch_year} году."

    def __str__(self) -> str:
        return f"{self.name} ({self.launch_year})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, launch_year={self.launch_year})"


class Satellite(Spacecraft):
    """
    Класс, описывающий спутник.

    Атрибуты:
        orbit (str): Тип орбиты (например, низкая, геостационарная).
    """

    def __init__(self, name: str, launch_year: int, orbit: str):
        super().__init__(name, launch_year)
        self.orbit = orbit

    def mission_info(self) -> str:
        """
        Возвращает информацию о спутнике.
        """
        return f"Спутник {self.name}, орбита: {self.orbit}, запуск: {self.launch_year}."

    def transmit_data(self) -> str:
        """Имитация передачи данных спутником."""
        return f"{self.name} передаёт данные с орбиты {self.orbit}."

    def __str__(self) -> str:
        return f"Спутник {self.name} ({self.orbit} орбита, {self.launch_year})"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, launch_year={self.launch_year}, "
                f"orbit={self.orbit!r})")


class Rover(Spacecraft):
    """
    Класс, описывающий ровер, находящийся на какой-либо планете.

    Атрибуты:
        planet (str): Планета или небесное тело, на котором работает ровер.
    """

    def __init__(self, name: str, launch_year: int, planet: str):
        super().__init__(name, launch_year)
        self.planet = planet

    def mission_info(self) -> str:
        """
        Перегрузка метода: миссия ровера уникальна тем, что он работает на поверхности.
        """
        return f"Ровер {self.name} исследует {self.planet} с {self.launch_year} года."

    def collect_samples(self) -> str:
        """Имитация сбора образцов почвы."""
        return f"{self.name} собирает образцы на {self.planet}."

    def __str__(self) -> str:
        return f"Ровер {self.name} на {self.planet} (запуск: {self.launch_year})"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, launch_year={self.launch_year}, "
                f"planet={self.planet!r})")


if __name__ == "__main__":
    # Создание экземпляров
    generic_spacecraft = Spacecraft("Explorer", 1998)
    hubble = Satellite("Hubble", 1990, "низкая околоземная")
    perseverance = Rover("Perseverance", 2020, "Марс")

    print(generic_spacecraft)
    print(hubble)
    print(perseverance)

    print()

    print(generic_spacecraft.mission_info())
    print(hubble.mission_info())
    print(hubble.transmit_data())
    print(perseverance.mission_info())
    print(perseverance.collect_samples())
