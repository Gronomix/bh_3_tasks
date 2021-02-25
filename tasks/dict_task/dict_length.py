"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть база с наименованиями товаров

Написать функцию products_num, которая возвращает количество наименований в базе

ПРИМЕРЫ
--------------------------------------------------------------------------------
products_num(PRODUCTS) -> 2
"""
PRODUCTS = {
    '112312': {
        'brand': 'Apple iPhone',
        'model': '11',
        'lib': '15'
    },
    '774554': {
        'brand': 'Samsung',
        'model': 'Galaxy S10'
    },
    '444555': {
        '555': 'ggg'

    },
}


def products_num(database: dict) -> int:

    result = len(PRODUCTS)
    return result


if __name__ == '__main__':
    print(f"Количество товаров в каталоге: {products_num(PRODUCTS)}")
