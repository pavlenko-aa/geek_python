from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, param):
        self.param = param


class Costume(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def count_cloth(self):
        return format(2 * self.param + 0.3, ".2f")


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def count_cloth(self):
        return format(self.param / 6.5 + 0.5, ".2f")


my_coat = Coat(48)
my_costume = Costume(179)

print(my_coat.count_cloth)
print(my_costume.count_cloth)
