"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая удалит элемент по его индексу
"""
from copy import deepcopy


def del_by_index(collection: list, index: int) -> list:
    collection_copy = deepcopy(collection)
    collection_copy.pop(2)
    return collection_copy


if __name__ == '__main__':
    assert 5 not in del_by_index([1, 3, 5, 2], 2)
    print('Решено!')
