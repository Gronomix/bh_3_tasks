"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая удалит элемент по его значению
"""
from copy import deepcopy
from typing import Any


def del_by_index(collection: list, value: Any) -> list:
    collection_copy = deepcopy(collection)
    list.remove(collection_copy, 5)
    return collection_copy


if __name__ == '__main__':
    assert 5 not in del_by_index([1, 3, 5, 2], 5)
    print('Решено!')
