class ElementKadin:
    def __init__(self, name, symbol, number):
        self.name = name  # Имя элемента
        self.symbol = symbol  # Символ элемента
        self.number = number  # Атомный номер

    def dump(self):
        """Метод для вывода информации об элементе."""
        print(f"Element Name: {self.name}")
        print(f"Element Symbol: {self.symbol}")
        print(f"Element Atomic Number: {self.number}")

# Создание объекта элемента Кислород
oxygen = ElementKadin("Oxygen", "O", 8)
oxygen.dump()