import doctest


class Cosmetics:
    def __init__(self, brand: str, made_in: str, exp: str, purpose: str):
        """
        Создание объекта "Косметика"
        :param brand: Бренд косметики
        :param made_in: Страна производителя
        :param exp: Срок годности
        :param purpose: Применение косметики
        """
        self._brand = brand
        self._made_in = made_in
        self._exp = exp
        self._purpose = purpose

    @property
    def brand(self):
        return self._brand

    @property
    def made_in(self):
        return self._made_in

    @property
    def exp(self):
        return self._exp

    @property
    def purpose(self):
        return self._purpose

    @brand.setter
    def brand(self, new_brand: str) -> None:
        if not isinstance(new_brand, str):
            raise TypeError("Бренд должен быть типа str")
        self._brand = new_brand

    @made_in.setter
    def made_in(self, new_made_in: str) -> None:
        if not isinstance(new_made_in, str):
            raise TypeError("Страна производителя должна быть типа str")
        self._made_in = new_made_in

    @exp.setter
    def exp(self, new_exp: str) -> None:
        if not isinstance(new_exp, str):
            raise TypeError("Срок годности должен быть типа str")
        self._exp = new_exp

    @purpose.setter
    def purpose(self, new_purpose: str) -> None:
        if not isinstance(new_purpose, str):
            raise TypeError("Применение должно быть типа str")
        self._purpose = new_purpose

    def __str__(self):
        return f"Бренд: {self.brand}. Производитель: {self.made_in}. Срок годности: {self.exp}. " \
               f"Применение: {self.purpose}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, country={self.made_in!r}, exp={self.exp!r}, " \
               f"pur={self.purpose!r})"

    def face(self) -> str:
        """
        Метод показывает, что косметика для лица
        :return: Косметика для лица
        """
        return self.purpose

    def year(self) -> str:
        """
        Метод выводит срок годности в виде года
        :return: Год до которого можно использовать продукцию
        """
        return self.exp


class Lipstick(Cosmetics):
    def __init__(self, brand: str, made_in: str, exp: str, purpose: str, texture: str):
        """
        Создание дочернего класса "Помада"
        :param brand: Бренд косметики
        :param made_in: Страна производителя
        :param exp: Срок годности
        :param purpose: Применение косметики
        :param texture: Текстура помады
        """
        super().__init__(brand, made_in, exp, purpose)
        self.texture = texture

    @property
    def texture(self):
        return self._texture

    @texture.setter
    def texture(self, new_texture: str) -> None:
        if not isinstance(new_texture, str):
            raise TypeError("Текстура помады должна быть типа str")
        self._texture = new_texture

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Текстура: {self.texture}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}(texture={self.texture!r})"

    def year(self):
        super_year = super().year()
        return f"{super_year}"

    def face(self):
        super().face()
        return f"Губы"


class Mascara(Cosmetics):
    def __init__(self, brand: str, made_in: str, exp: str, purpose: str, volume: int):
        """
          Создание дочернего класса "Тушь"
          :param brand: Бренд косметики
          :param made_in: Страна производителя
          :param exp: Срок годности
          :param purpose: Применение косметики
          :param volume: Объем упаковки
          """
        super().__init__(brand, made_in, exp, purpose)
        self.volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume: int) -> None:
        if not isinstance(new_volume, int):
            raise TypeError("Объем упковки должен быть типа int")
        self._volume = new_volume

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Объем упаковки: {self.volume}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}(volume={self.volume!r})"

    def year(self):
        super_year = super().year()
        return f"{super_year}"

    def face(self):
        super().face()
        return f"Глаза"


if __name__ == "__main__":
    cosmetics = Cosmetics("Chanel", "Франция", "2025", "Лицо")
    print(cosmetics.brand)
    print(cosmetics.year())
    print(cosmetics.face())
    lip = Lipstick("Clarins", "Франция", "2024", "Лицо", "Жидкая")
    print(lip.made_in)
    print(lip.year())
    print(lip.face())
    eyes = Mascara("Dior", "Франция", "2026", "Лицо", 10)
    print(eyes.brand)
    print(eyes.face())
    print(eyes.year())
    print(eyes.volume)
    doctest.testmod()
    pass
