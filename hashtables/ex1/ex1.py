#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    result = []
    if len(weights) <= 1:
        return None
    
    for i in weights:
        difference = limit - i
        hash_table_insert(ht, difference, i)

    for j, i in enumerate(weights):
        if hash_table_retrieve(ht, i) == limit - i:
            result.insert(0, j)
    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
