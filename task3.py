"""Создайте класс Rectangle с длиной и шириной. И методы для получения площади и периметра. Также проперти метод для получения полной информации про прямоугольник.  Используйте инкапсуляцию для длины и ширины.
/"""



class Rectangle:
    """Атрибут к прямоугольнику: длина и ширина"""
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    #Нахождение площадь прямоугольника
    def square(self):
        return self._length * self._width

    # Нахождение периметра прямоугольника
    def perimeter(self):
        return (self._length + self._width) * 2


    @property

    def show_all(self):
        return self._length and self._width

    def set_length(self, new_length: int):
        self._length = new_length

    def set_width(self, new_width: int):
        self._width = new_width

    def get_all(self):
        return self._length and self._width

a = Rectangle(1, 4)