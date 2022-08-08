'''metaclass_ex.py'''

from collections import namedtuple
from typing import List


Edge = namedtuple('Edge', ['from_', 'to_'])


def y_algorithm(arr_: List[Edge]) -> List[str]:
    '''Алгоритм формирования маршрута'''

    edge = arr_.pop()
    start, end = list(edge)
    queue_ = [start, end]

    while len(arr_) > 0:
        for edge in arr_:
            print(queue_, ' <- ', edge)
            from_, to_ = edge
            if from_ == end:
                end = to_
                queue_.append(to_)
                arr_.remove(edge)
            elif to_ == start:
                start = from_
                queue_.insert(0, from_)
                arr_.remove(edge)

    return queue_


def y_algorithm_modified(arr_: List[Edge]) -> List[str]:
    '''Алгоритм формирования маршрута один проход'''

    edge = arr_.pop()
    queue_ = [list(edge)]

    departure = [edge.from_]
    arrival = [edge.to_]

    while len(arr) > 0:
        edge = arr_.pop()
        print(queue_, ' <- ', edge)

        if edge.from_ in arrival:
            ind = arrival.index(edge.from_)
            queue_[ind].append(edge.to_)
            arrival[ind] = edge.to_

            if edge.to_ in departure:
                ind_ = departure.index(edge.to_)
                queue_[ind].extend(queue_[ind_][1:])
                queue_.remove(queue_[ind_])
                arrival[ind] = arrival[ind_]
                departure.pop(ind_)
                arrival.pop(ind_)
        else:
            if edge.to_ in departure:
                queue_[departure.index(edge.to_)].insert(0, edge.from_)
                departure[departure.index(edge.to_)] = edge.from_
            else:
                queue_.append(list(edge))
                departure.append(edge.from_)
                arrival.append(edge.to_)

    return queue_[0]


arr = [Edge(d['from'], d['to'])
        for d in [{'from': 'A', 'to': 'B'},
                  {'from': 'D', 'to': 'E'},
                  {'from': 'C', 'to': 'D'},
                  {'from': 'Z', 'to': 'A'},
                  {'from': 'F', 'to': 'G'},
                  {'from': 'B', 'to': 'C'},
                  {'from': 'E', 'to': 'F'},
                  {'from': 'Y', 'to': 'Z'},
                  {'from': 'X', 'to': 'Y'}]]


# res = y_algorithm_modified(arr)
res = y_algorithm(arr)
print(res)
