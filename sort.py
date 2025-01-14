
def insertion_sort(data, key_index, dec=False):
    """
    Sorts a list of dictionaries based on a specified key using insertion sort.

    :param data: List of dictionaries to sort.
    :param key_index: Key to sort the dictionaries by.
    :param descending: If True, sorts in descending order. Default is ascending.
    """
    for i in range(1, len(data)):
        key_item = data[i]
        key_value = key_item[key_index]

        # Find the correct position for the current item
        j = i - 1
        while j >= 0 and (
            (data[j][key_index] > key_value if not dec else data[j][key_index] < key_value)
        ):
            data[j + 1] = data[j]  # Shift the element one position to the right
            j -= 1

        # Place the key_item in its correct position
        data[j + 1] = key_item

    return data
