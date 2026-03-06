# 0. Utils
# 1. Linear Search
# 2. Binary Search
# 3. Jump Search

import random

def generate_random_unsorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    """
    Generate random and unsorted list with count n.
    
    n : List item count
    min_value : minimum random value
    max_value : maximum random value
    """
    new_list = []
    for i in range(n):
        new_list.append(random.randint(min_value,max_value))

    return new_list
def generate_random_sorted_list(n:int=20, min_value:int=0, max_value:int=1000)->list:
    
    new_list = []
    last_added = 0
    new_value = 0
    
    for i in range(n):
        # TODO Refine min/max value issue
        new_value = random.randint(last_added+1, max(last_added+10,max_value))
        new_list.append(new_value)
        last_added = new_value
    
    return new_list
    
        
   
print(generate_random_sorted_list())