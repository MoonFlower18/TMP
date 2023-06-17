from abc import ABC, abstractmethod
from typing import List

class sweetsItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"конфетка под номером: {self.number}"


class Iterator(ABC):
    @abstractmethod
    def next(self) -> sweetsItem:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...

class sweetsnumIterator(Iterator):
    def __init__(self, sweets: List[sweetsItem]):
        self._sweets = sweets
        self._index = 0

    def next(self) -> sweetsItem:
        sweets_item = self._sweets[self._index]
        self._index += 1
        return sweets_item

    def has_next(self) -> bool:
        return False if self._index >= len(self._sweets) else True

class sweetsAggregate:
    def __init__(self, amount_num: int = 10):
        self.num = [sweetsItem(it+1) for it in range(amount_num)]
        print(f"Взяли чашку с конфетами "
              f"на {amount_num} конфеток")

    def amount_num(self) -> int:
        return len(self.num)

    def iterator(self) -> Iterator:
        return sweetsnumIterator(self.num)

if __name__ == "__main__":
    sweets = sweetsAggregate(5)
    iterator = sweets.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))