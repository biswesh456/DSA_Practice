from typing import List
from copy import deepcopy

def power(lst: List):
    power_set = [[]]
    for i in lst:
        p_copy = deepcopy(power_set)
        for p in p_copy:
            p.append(i)
            power_set.append(p)
    
    return power_set

print(power([2,3,4]))