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
    if len(weights) <= 1:
        return None

    result = []
    table = {}
    for i in weights:
        difference = limit - i
        table[i] = difference

    for i, j in enumerate(weights):
        if limit - j in table:
            result.insert(0, i)

    return result


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
