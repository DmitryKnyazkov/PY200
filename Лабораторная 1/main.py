import doctest


class KarkasnyiDom:
    def __init__(self, etazi: int, zil_plosyad: float | int, stoimost_dereva: float | int, stoimost_uteplitelya: float|int):
        """
        Создание объекта "Каркасный Дом"
        :param etazi: количество этажей в доме
        :param zil_plosyad: Жилая площадь дома
        :param stoimost_dereva: стоимость деревянных материалов
        :param stoimost_uteplitelya: стоимость утеплителя

        Примеры:
        >>> karkas_dom = KarkasnyiDom(3,100.4,1000000, 500000) # инициализация экземпляра класса
        """
        self.proverka_etazey(etazi)
        self.etazi = etazi
        self.proverka_ostalnogo(zil_plosyad)
        self.proverka_ostalnogo(stoimost_dereva)
        self.proverka_ostalnogo(stoimost_uteplitelya)
        self.zil_plosyad = zil_plosyad
        self.stoimost_dereva = stoimost_dereva
        self.stoimost_uteplitelya = stoimost_uteplitelya



    def proverka_etazey(self, etazi) -> None:
        '''
        Проверка корректности передачи информации по этажности дома
        '''
        if not isinstance(etazi, int):
            raise TypeError("Этажи д.б. Int")
        if etazi < 1 or etazi > 3:
            raise ValueError("Этажей д.б. от 1 до 3")

    def proverka_ostalnogo(self, proverka: float|int) -> None:
        """
        Проверка корректрности переданной информации по жилой площади дома, стоимости деревянных материалов
        и утеплителя. Поскольку все они должны быть float или int, то проверочный метод один на всех.
        """
        if not isinstance(proverka, float | int):
            raise TypeError("Жилая площадь, и стоимость материалов должны быть float или int")
        if proverka < 0:
            raise ValueError("информация по жилой площади дома, стоимости деревянных материалов и утеплителя не д.б. отрицательной")


    def stoimost_materialov(self) -> float|int:
        """
        Метод, который возращает стоимость материалов дома.

        :return float|int

        Примеры:
        >>> karkas_dom = KarkasnyiDom(2,100.4,1000000, 500000) # инициализация экземпляра класса
        >>> karkas_dom.stoimost_materialov()
        """
        return self.stoimost_dereva + self.stoimost_uteplitelya

    def stoimost_metra(self) -> float|int:
        """
        Метод, который возращает стоимость квадратного метра дома (экземпляра)
        Примеры:
        >>> karkas_dom = KarkasnyiDom(2,100.4,1000000, 500000) # инициализация экземпляра класса
        >>> karkas_dom.stoimost_metra()
        """
        return (self.stoimost_dereva + self.stoimost_uteplitelya)/self.zil_plosyad



class BrusovyiDom:
    def __init__(self, etazi: int, zil_plosyad: (float | int), stoimost_brusa: (float | int)):
        '''
        Создание объекта "Брусовый Дом"
        :param etazi: количество этажей в доме
        :param zil_plosyad: Жилая площадь дома
        :param stoimost_brusa: стоимость деревянных материалов


        Примеры:
        >>> brus_dom = BrusovyiDom(3,100.4,1000000) # инициализация экземпляра класса
        '''

        self.etazi = None
        self.set_etaz(etazi)

        self.proverka_ostalnogo(zil_plosyad)
        self.proverka_ostalnogo(stoimost_brusa)

        self.zil_plosyad = zil_plosyad
        self.stoimost_brusa = stoimost_brusa




    def proverka_etazey(self, etazi: int) -> None:
        '''
        Проверка корректности передачи информации по этажности дома
        '''
        if not isinstance(etazi, int):
            raise TypeError("Этажи д.б. Int")
        if etazi < 1 or etazi > 5:
            raise ValueError("Этажей д.б. от 1 до 5")

    def proverka_ostalnogo(self, proverka: float | int) -> None:
        """
        Проверка корректрности переданной информации по жилой площади дома, стоимости деревянных материалов.
        Поскольку все они должны быть положительными и быть float или int, то проверочный метод один на всех.
        """
        if not isinstance(proverka, float | int):
            raise TypeError("Жилая площадь, и стоимость материалов должны быть float или int")
        if proverka < 0:
            raise ValueError("информация по жилой площади дома и стоимости деревянных материалов не д.б. отрицательной")

    def set_etaz(self, etazi: int) -> None:
        """
        Этот метод определяет этажность дома.

        :param etazi: Это этажность дома

        Пример:
        >>> brus_dom = BrusovyiDom(3,100.4,1000000) # инициализация экземпляра класса
        >>> brus_dom.set_etaz(2) # меняем экземпляру этажность
        """
        self.proverka_etazey(etazi)
        self.etazi = etazi


    def stoimost_materialov(self) -> float | int:
        """
        Метод, который возращает стоимость материалов дома. В данном случае только стоимость бруса.

        :return: float | int

        Примеры:
        >>> karkas_dom = KarkasnyiDom(2,100.4,1000000, 500000) # инициализация экземпляра класса
        >>> karkas_dom.stoimost_materialov()
        """
        return self.stoimost_brusa

    def stoimost_metra(self) -> float | int:
        """
        Метод, который возращает стоимость квадратного метра дома (экземпляра)
        Примеры:
        >>> karkas_dom = KarkasnyiDom(2,100.4,1000000, 500000) # инициализация экземпляра класса
        >>> karkas_dom.stoimost_metra()
        """
        return self.stoimost_brusa/self.zil_plosyad

    def __repr__(self):
        return f"Этажность {self.etazi}, Жилая площадь {self.zil_plosyad}, Стоимость бруса {self.stoimost_brusa}, Стоимость метра квадратного жилья {self.stoimost_metra()}"


class KirpichnyiDom:
    """
    Создание объекта "Кирпичный дом"
    """
    def __init__(self, etazi, stoimost_kirpicha, kirpichey_na_etaz=1000):
        '''
        :param etazi: количество этажей
        :param stoimost_kirpicha: Стоимость кирпича
        :param kirpichey_na_etaz: кирпичей на этаж

        Пример:
        >>> big_kir_dom = KirpichnyiDom(5, 1) # инициализируем экземпляр класса
        '''

        self.etazi = None
        self.set_etaz(etazi)
        self.stoimost_kirpicha = None
        self.set_stoimost_kirpicha(stoimost_kirpicha)
        self.kirpichey_na_etaz = kirpichey_na_etaz

    def proverka_etazey(self, etazi) -> None:
        '''
        Проверка корректности передачи информации по этажности дома
        '''
        if not isinstance(etazi, int):
            raise TypeError("Этажи д.б. Int")
        if etazi < 1 or etazi > 16:
            raise ValueError("Этажей д.б. от 1 до 16")



    def set_etaz(self, etazi):
        """
        Этот метод определяет этажность дома.

        :param etazi: Это этажность дома

        Пример:
        >>> self.set_etaz(etazi)
        """
        self.proverka_etazey(etazi)
        self.etazi = etazi

    def proverka_stoimost_kirpicha(self, stoimost_kirpicha: float | int):
        """
        Проверка корректрности переданной информации по стоимости кирпича.
        """
        if not isinstance(stoimost_kirpicha, float | int):
            raise TypeError("Стоимость кирпича должны быть float или int")
        if stoimost_kirpicha < 0:
            raise ValueError("Стоимость кирпича не д.б. отрицательной")

    def set_stoimost_kirpicha(self, stoimost_kirpicha) -> None:
        '''
        Определяет стоимость кирпича
        '''
        self.proverka_stoimost_kirpicha(stoimost_kirpicha)
        self.stoimost_kirpicha = stoimost_kirpicha


    def proverka_kirpichey_na_etaz(self, kirpichey_na_etaz) -> None:
        """
        Проверка корректрности переданной информации по кирпичам на этаж.
        """
        if not isinstance(kirpichey_na_etaz, float | int):
            raise TypeError("Стоимость кирпича должны быть float или int")
        if kirpichey_na_etaz < 0:
            raise ValueError("Стоимость кирпича не д.б. отрицательной")

    def set_kirpichey_na_etaz(self, kirpichey_na_etaz):
        '''
        Метод определяет количество кирпичей для одного этажа дома
        '''
        self.proverka_kirpichey_na_etaz(kirpichey_na_etaz)
        self.kirpichey_na_etaz = kirpichey_na_etaz


    def stoimost_doma(self):
        '''
        Метод определяет стоимость дом исходя из количества этажей, стоимости кирпичей и коичества кирпичей
        на этаж
        '''
        return self.etazi * self.stoimost_kirpicha * self.kirpichey_na_etaz

    def __repr__(self):
        return f'Этажей{self.etazi}, Стоимость кирпича {self.stoimost_kirpicha}, Количество кирпичей на этаж {self.kirpichey_na_etaz}, Стоимость Дома {self.stoimost_doma()}'

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    print("Первый класс")
    big_house = KarkasnyiDom(3,300,3000000, 2000000)
    medium_house = KarkasnyiDom(2, 200, 1500000, 1000000)
    print(f'Стоимость материалов {big_house.stoimost_materialov()}')
    print("заменим стоимость утеплителя")
    big_house.stoimost_uteplitelya = 5000000
    print(f'Стоимость материалов {big_house.stoimost_materialov()}')
    print(f'Стоимость метра квадратного {big_house.stoimost_metra()}')
    print(f'Стоимость метра квадратного второго экземпляра {medium_house.stoimost_metra()}')
    print("  ")

    print("Второй класс")
    big_br_dom = BrusovyiDom(5, 180.5, 5000000)
    medium_br_dom = BrusovyiDom(3, 100, 3000000)

    print(big_br_dom)
    big_br_dom.set_etaz(4) # заменим этажность дома
    print("Заменим этажность дома")
    print(big_br_dom)
    print("")
    print(medium_br_dom)
    print('')

    print('Третий класс')
    big_kir_dom = KirpichnyiDom(10, 2, 7000)
    print(f'Стоимость дома {big_kir_dom.stoimost_doma()}')
    print(big_kir_dom)
    print("заменим этажность на 15")
    big_kir_dom.set_etaz(15)
    print(big_kir_dom)
