import doctest


class Box:
    def __init__(self, color : str, material : str, occupy : int ):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param color: цвет коробки
        :param material: материал коробки
        :param capacity: заполненность коробки
        """

        if not isinstance(color, str):
            raise TypeError('Цвет должен быть типа str')
        self.color = color

        if not isinstance(material, str):
            raise TypeError('Материал должен быть типа str')
        self.material = material

        if not isinstance(occupy, int):
            raise TypeError('Заполненность коробки должна быть типа int')
        self.occupy = occupy

    def is_box_empty(self) -> bool:
        """
        Функция которая проверяет является ли коробка пустой
        :return: Является ли коробка пустой
        """
        ...

    def is_box_glass(self) -> bool:
        """
        Функция которая проверяет является ли коробка стеклянной
        :return: Является ли коробка стеклянной
        """
        ...

if __name__ == "__main__":
    box = Box ('синий', 'стекло', 0)
    box.is_box_empty()
    box = Box('синий', 'стекло', 0)
    box.is_box_glass()
    doctest.testmod()

class Tea:
    def __init__(self, taste : str, pack : str):
        """
        Создание и подготовка к работе объекта "Чай"
        :param taste: вкус чая
        :param pack: упаковка - пакетики
        """

        if not isinstance(taste, str):
            raise TypeError('Вкус должен быть типа str')
        self.taste = taste

        if not isinstance(pack, str):
            raise TypeError('Упаковка должна быть типа str')
        self.pack = pack

    def tea_taste(self) -> None:
        """
        Функция которая показывает, что чай черный
        :return: Черный чай
        """
        ...

    def tea_pack(self) -> None:
        """
        Функция которая показывает, что упаковка- пакетики
        :return: Упаковка-пакетики
        """
        ...

if __name__ == "__main__":
    tea = Tea ('черный', 'пакетики')
    tea.tea_taste()
    tea = Tea('черный', 'пакетики')
    tea.tea_pack()
    doctest.testmod()

class Table:
    def __init__(self, lenght : int, width : int, height : int):
        """
        Создание и подготовка к работе объекта "Стол"
        :param lenght: длина стола
        :param width: ширина стола
        :param height: высота стола
        """

        if not isinstance(lenght, int):
            raise TypeError('Длина должна быть типа int')
        if lenght <= 0:
            raise ValueError('Длина не может быть отрицательным числом')
        self.lenght = lenght

        if not isinstance(width, int):
            raise TypeError('Ширина должна быть типа int')
        if width <= 0:
            raise ValueError('Ширина не может быть отрицательным числом')
        self.width = width

        if not isinstance(height, int):
            raise TypeError('Высота должна быть типа int')
        if height <= 0:
            raise ValueError('Высота не может быть отрицательным числом')
        self.height = height

    def table_is_lenght(self, lenght) -> None:
        """
        Функция показывает, что стол длинный, если длина больше 100
        :param lenght: длина стола
        :return: стол длинный
        """
        if lenght > 100:
            raise('Стол длинный')
        ...

    def table_is_width (self, width) -> None:
        """
        Функция показывает, что стол широкий, если ширина больше 150
        :param width: ширина стола
        :return: стол широкий
        """
        if width > 150:
            raise('Стол широкий')
        ...

    def table_is_height(self, height) -> None:
        """
        Функция показывает, что стол высокий, если высота больше 60
        :param height: высота стола
        :return: стол высокий
        """
        if height > 65:
            raise ('Стол высокий')

if __name__ == "__main__":
    table = Table(101, 100, 55)
    table.table_is_lenght(100)
    table = Table(100, 151, 55)
    table.table_is_width(150)
    table = Table(100, 140, 65)
    table.table_is_height(60)
    doctest.testmod()
