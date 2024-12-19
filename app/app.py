class Parallelogram():
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        if value <= 0:
            raise ValueError("Сторона a должна быть больше нуля.")
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        if value <= 0:
            raise ValueError("Сторона b должна быть больше нуля.")
        self.__side_b = value

    @staticmethod
    def about():
        print(
            "Данную работу сделали Кузьменко И.Е. как разработчик №1, Бархазов А.Р. как разработчик №2 и Кадин А.А.  разработчик №3")

    def calc_perimeter(self):
        """Метод для расчета периметра параллелограмма"""
        return 2 * (self.side_a + self.side_b)


# Главная программа
def main():
    print("Введите длины сторон параллелограмма:")
    try:
        side_a = float(input("Сторона a: "))
        side_b = float(input("Сторона b: "))

        # Создание объекта параллелограмма
        parallelogram = Parallelogram(side_a, side_b)

        # Вывод периметра
        print(f"Периметр параллелограмма равен {parallelogram.calc_perimeter()} единиц.")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
