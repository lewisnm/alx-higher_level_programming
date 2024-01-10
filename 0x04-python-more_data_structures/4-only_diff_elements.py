#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.intersection(set_2)
    set3 = set_1.union(set_2)
    z = list(new_set)
    for z in z:
        if z in set3:
            set3.remove(z)
    return set3
