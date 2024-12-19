class ElementBahrazov:
    def __init__(self, name, symbol, number):
        self.__name = name  # Приватный атрибут для имени
        self.__symbol = symbol  # Приватный атрибут для символа
        self.__number = number  # Приватный атрибут для атомного номера

    @property
    def name(self):
        """Свойство для получения имени элемента."""
        return self.__name

    @property
    def symbol(self):
        """Свойство для получения символа элемента."""
        return self.__symbol

    @property
    def number(self):
        """Свойство для получения атомного номера элемента."""
        return self.__number

    def dump(self):
        """Метод для вывода информации об элементе."""
        print(f"Element Name: {self.name}")
        print(f"Element Symbol: {self.symbol}")
        print(f"Element Atomic Number: {self.number}")

# Создание объекта элемента Берилий
beryllium = ElementBahrazov("Beryllium", "Be", 4)
beryllium.dump()
