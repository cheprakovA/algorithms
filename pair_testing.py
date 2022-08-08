'''
Алгоритм парного тестирования
'''

import itertools
import collections
from typing import Set


data = list(itertools.product(*[(0, 1, 2), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]))
combinations = [tuple(itertools.combinations(c, 2)) for c in data]

pairs_repeat = []


for row in list(map(tuple, zip(*combinations))):
    d = collections.defaultdict(set)
    for i, _ in enumerate(row):
        d[row[i]].add(i)
    pairs_repeat.append(d)


not_visited = list(range(len(combinations)))
visited: Set[int] = set()
result: Set[int] = set()


while len(visited) + len(result) < len(not_visited):
    ind = not_visited[min(filter(lambda x: x not in (list(visited) + list(result)), not_visited))]
    result.add(ind)
    nv_indexes = list(filter(lambda x: x not in (list(visited) + list(result)), not_visited))

    # print(ind)
    # print(list(nv_indexes))

    redurant = set()

    # step 1
    for i in nv_indexes:
        for j in range(len(combinations[i])):
            # if ind in pairs_repeat[j][combinations[ind][j]]:
            #     pairs_repeat[j][combinations[ind][j]].remove(ind)
            # print((i, j), pairs_repeat[j][combinations[ind][j]])
            # pairs_repeat[j][combinations[ind][j]].remove(ind)
            # if len(pairs_repeat[j][combinations[ind][j]]) == 1:
            #     pass

            if combinations[i][j] == combinations[ind][j]:
                visited.add(i)
                for k in pairs_repeat[j][combinations[i][j]]:
                    redurant.add(k)

            # if len(pairs_repeat[j][combinations[i][j]]) == 1:
            #     solo_index = pairs_repeat[j][combinations[i][j]][0]
            #     result.add(solo_index)

    redurant_ = set()

    # step 2
    for d in pairs_repeat:
        for k, v in d.items():
            d[k] = v - redurant

            if len(d[k]) == 1:
                redurant_.add(d[k].pop())

        for k in list(d):
            if len(d[k]) == 0:
                del d[k]

    # # step 3
    # for elem in redurant_:
    #     result.add(elem)

    # for _ind in redurant_:
    #     _indexes = list(filter(lambda x: x not in (list(visited) + list(result)), not_visited))
    #     for i in _indexes:
    #         for j in range(len(combinations[i])):
    #             if combinations[i][j] == combinations[_ind][j]:
    #                 visited.add(i)

        
    # nv_indexes = list(filter(lambda x: x not in (list(visited) + list(result)), not_visited))




print(*[data[i] for i in sorted(list(result))], sep='\n')
