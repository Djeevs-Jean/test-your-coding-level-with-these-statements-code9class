DATA_LIST = [0, 1, 2, 3, 4]

def reverse_seq_list(listes:list, fin_value):
    length = list(range(1, len(listes)+1))[::-1]
    for i in length:
        liste_1 = listes
        listes = list(reversed(listes[:i])) + listes[i:]
        print(f"{liste_1} -> {listes}")
    print("index: {} value: {}".format(listes.index(fin_value), listes[listes.index(fin_value)]))

reverse_seq_list(DATA_LIST, 3)

"""
[0, 1, 2, 3, 4] -> [4, 3, 2, 1, 0]
[4, 3, 2, 1, 0] -> [1, 2, 3, 4, 0]
[1, 2, 3, 4, 0] -> [3, 2, 1, 4, 0]
[3, 2, 1, 4, 0] -> [2, 3, 1, 4, 0]

0 1 2 3 4 -> 4 3 2 1 0
4 3 2 1 0 -> 1 2 3 4 0
1 2 3 4 0 -> 3 2 1 4 0
3 2 1 4 0 -> 2 3 1 4 0

"""
