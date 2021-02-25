"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть база WORKERS с днями рождений сотрудников

Написать функцию get_workers, которая возвращает
элементы (ключ-значение) в словаре WORKERS
"""
WORKERS = {
    'Декоратор Иван Олегович': '13.05.1980',
    'Баг Илья Андреевич': '07.09.1995',
    'Питонов Петр Сергеевич': '25.12.1991',
    'Асинхронова Алла Анатольевна': '05.01.1987',
}


def get_workers(workers: dict):

    result = dict.items(WORKERS)
    return result


if __name__ == '__main__':
    print('Дни рождения сотрудников:')
    for worker, date_of_birth in get_workers(WORKERS):
        print(f"- {worker}: {date_of_birth}")
