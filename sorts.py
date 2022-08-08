'''
sorts.py
'''

from math import log2


def insertion_sort(arr_):
    '''Сортировка вставками'''

    for i, curr in enumerate(arr_[1:]):
        loc = i - 1
        while loc >= 0 and arr_[loc] > curr:
            arr_[loc+1] = arr_[loc]
            loc -= 1
        arr_[loc+1] = curr
        print(arr_)


def _binary_search(arr_, insertion):
    '''Бинарный поиск'''

    first, last, mid = 0, len(arr_), 0
    while first < last:
        mid = (last + first) // 2
        if insertion < arr_[mid]:
            last = mid
        else:
            first = mid + 1
    return first


def insertion_sort_task4(arr_):
    '''
    При внимательном изучении алгоритма InsertionSort видно, что вставка нового элемента
    основана на алгоритме последовательного поиска. В главе 2 мы показали, что двоичный поиск
    гораздо эффективнее. Модифицируйте сортировку вставками, применив двоичный поиск места
    вставки нового элемента. Обратите внимание на то, что при уникальных значениях ключей
    стандартный двоичный поиск всегда заканчивается неудачей.
    Замените стандартный поиск функцией, возвращающей значение искомой позиции.
    '''

    for i, curr in enumerate(arr_):
        if i == 0:
            continue
        loc = _binary_search(arr_[:i], curr)
        for j in range(i, loc, -1):
            arr_[j] = arr_[j-1]
        arr_[loc] = curr


def bubble_sort(arr_):
    '''Пузырьковая сортировка'''

    swapped = True
    last = len(arr_) - 1
    while swapped:
        swapped = False
        for i in range(last):
            if arr_[i] > arr_[i+1]:
                arr_[i], arr_[i+1] = arr_[i+1], arr_[i]
                swapped = True
        last -= 1


def bubble_sort_task3(arr_):
    '''
    Еще в одном варианте пузырьковой сортировки запоминается информация о том,
    где произошел последний обмен элементов, и при следующем проходе алгоритм не заходит
    за это место. Если последними поменялись i-ый и i+1-ый элементы, то при следующем
    проходе алгоритм не сравнивает элементы за i-м.
    '''

    swapped = True
    last = len(arr_) - 1
    while swapped:
        swapped = False
        for i in range(last):
            if arr_[i] > arr_[i+1]:
                arr_[i], arr_[i+1] = arr_[i+1], arr_[i]
                swapped = True
                last = i


def bubble_sort_task4(arr_):
    '''
    Еще в одном варианте пузырьковой сортировки нечетные и четные проходы выполняются
    в противоположных направлениях: нечетные проходы в том же направлении, что и в
    исходном варианте, а четные — от конца массива к его началу. При нечетных проходах
    большие элементы сдвигаются к концу массива, а при четных проходах —
    меньшие элементы двигаются к его началу.
    '''

    swapped = True
    odd = True
    first, last = 0, len(arr_) - 1
    while swapped:
        swapped = False
        if odd:
            for i in range(first, last):
                if arr_[i] > arr_[i+1]:
                    arr_[i], arr_[i+1] = arr_[i+1], arr_[i]
                    swapped = True
            last -= 1
            odd = False
        else:
            for i in range(last, first, -1):
                if arr_[i-1] > arr_[i]:
                    arr_[i-1], arr_[i] = arr_[i], arr_[i-1]
                    swapped = True
            first += 1
            odd = True


def bubble_sort_task5(arr_):
    '''
    В третьем варианте пузырьковой сортировки идеи первого и второго измененных
    вариантов совмещены. Этот алгоритм двигается по массиву поочередно вперед и
    назад и дополнительно выстраивает начало и конец списка в зависимости от
    места последнего изменения.
    '''

    swapped = True
    odd = True
    first, last = 0, len(arr_) - 1
    while swapped:
        swapped = False
        if odd:
            for i in range(first, last):
                if arr_[i] > arr_[i+1]:
                    arr_[i], arr_[i+1] = arr_[i+1], arr_[i]
                    swapped = True
                    last = i
            odd = False
        else:
            for i in range(last, first, -1):
                if arr_[i-1] > arr_[i]:
                    arr_[i-1], arr_[i] = arr_[i], arr_[i-1]
                    swapped = True
                    first = i
            odd = True


def _insertion_sort_by_step(arr_, first_, step_):
    '''Сортировка вставками для групп'''

    indexes = list(range(first_, len(arr_), step_))
    for k, _ in enumerate(indexes):
        curr = arr_[indexes[k]]
        if k == 0:
            continue
        loc = k - 1
        while loc >= 0 and arr_[indexes[loc]] > curr:
            arr_[indexes[loc+1]] = arr_[indexes[loc]]
            loc -= 1
        arr_[indexes[loc+1]] = curr


def shell_sort(arr_):
    '''Сортировка Шелла'''

    passes = int(log2(len(arr_)))
    while passes >= 1:
        step = pow(2, passes-1)
        for start in range(step):
            _insertion_sort_by_step(arr_, start, step)
        passes -= 1


arr = list(range(16))[::-1]


