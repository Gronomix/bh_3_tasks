"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая добавляет элемент в конец списка
"""
from copy import deepcopy
from typing import Any


def add(collection: list, element: Any) -> list:
    collection_copy = deepcopy(collection)
    # TODO вставить код сюда
    return collection_copy


if __name__ == '__main__':
    assert add([1, 2, 3], 2) == [1, 2, 3, 2]
    assert add([1, 2, 3], 5) == [1, 2, 3, 5]
    print('Решено!')
