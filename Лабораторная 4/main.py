from abc import ABC, abstractmethod

class Tableware(ABC):
    """
    Абстрактный класс для посуды
    """
    @abstractmethod
    def __init__(self, material: str =None, color: str =None):
        """
        конструктор абстрактного класса
        """
        self.material = material
        self.color = color


    def __str__(self):
        return f"{self.__class__.__name__}"

    @abstractmethod
    def __repr__(self):
        ...

class Plate(Tableware):
    """
    дочерний класс тарелка родительского класса посуда
    """
    def __init__(self, diametr: int | float, material: str, color: str):
        super().__init__(material, color)
        self._diametr = diametr #протектет - просто так решил

    @property
    def diametr(self):
        return self._diametr

    @diametr.setter
    def diametr(self, diametr):
        self._diametr = diametr

    def __repr__(self):
        return f"{self.__class__.__name__}(diametr={self._diametr}, material={self.material}, color={self.color})"

class Cup(Tableware):
    """
    дочерний класс кружка родительского класса посуда
    """
    def __init__(self, volume: int|float, material: str, color: str):
        super().__init__(material, color)
        self.volume = volume

    def __repr__(self):
        return f"{self.__class__.__name__}(diametr={self.volume}, material={self.material}, color={self.color}, {self._weight_cup(10)})"

    def _weight_cup(self, volume: int|float) -> int|float:
        """
        протектет метод. что-то очень важное считает.
        """
        weight_cup = volume * 0.7 / 2 + volume**2
        return weight_cup

if __name__ == "__main__":
    a = Plate(diametr=2, material="wood", color="blue")
    print(a)
    print(repr(a))

    b = Cup(4,"metal", "red")
    print(b)
    print(repr(b))
    print()
    print(a.diametr)
    a.diametr = 1000
    print(repr(a))
    print()
