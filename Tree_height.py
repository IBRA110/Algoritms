"""
Высота дерева
Вычислить высоту данного дерева.
Вход.
Корневое дерево с вершинами{0, . . . , n−1}, 
заданноекак последовательностьparent0, . . . ,parentn−1, где
parenti—родительi-й вершины.Выход.Высота дерева.
3
Деревья имеют огромное количество при-менений в Computer Science. 
Они используютсякак для представления данных, 
так и во мно-гих алгоритмах машинного обучения. 
Далеемы также узнаем, как сбалансированные де-ревья используются для 
реализации словарей и ассоциативных массивов. 
Данные структуры данных так или иначе используются во всех языках 
программирования и базах данных.Ваша цель в данной задаче — научиться хранить и 
эффективно об-рабатывать деревья, даже если в них сотни тысяч вершин.
Формата входа.Первая строка содержит натуральное число n.
Вторая строка содержит n целых неотрицательных чисел parent0, . . . ,parent n−1. 
Для каждого0≤i≤n−1,parenti—родитель вершиныi; 
если parenti=−1, то i является корнем.
Гарантируется, что корень ровно один. 
Гарантируется, чтоданная последовательность задаёт дерево.
Формат выхода. Высота дерева.
Ограничения.1≤n≤105

Sample Input:
10
9 7 5 5 2 9 9 9 2 -1

Sample Output:
4
"""

# Решение

def _tree(tree):
    town = {i: set() for i in range(len(tree))}
    town[-1] = set()
    for i in range(len(tree)):
        town[tree[i]].add(i)
    root, l = town[-1], 0
    while len(root):
        q, root = root, []
        for i in q:
            root += town[i]
        l += 1
    return l

def main():
    n, tree = int(input()), [int(i) for i in input().split()]
    assert n == len(tree)
    print(_tree(tree))


if __name__ == '__main__':
    main()