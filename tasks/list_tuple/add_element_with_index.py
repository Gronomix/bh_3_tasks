"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая добавляет элемент на указанную позицию
"""
from copy import deepcopy
from typing import Any


def add_by_index(collection: list, index: int, element: Any) -> list:
    collection_copy = deepcopy(collection)
    # TODO вставить код сюда
    return collection_copy


if __name__ == '__main__':
    assert add_by_index([1, 2, 3], 2, 5) == [1, 2, 5, 3]
    print('Решено!')
