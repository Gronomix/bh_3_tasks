"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая очистит список
"""
from copy import deepcopy


def clear_list(collection: list) -> list:
    collection_copy = deepcopy(collection)
    # TODO вставить код сюда
    return collection_copy


if __name__ == '__main__':
    assert clear_list([1, 2, 3]) == []
    print('Решено!')
