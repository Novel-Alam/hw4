def merge_list(list1, list2):
    # Merge the two lists
    list3 = list1 + list2

    # Check if all elements are integers
    for i in list3:
        if not isinstance(i, int):
            raise TypeError("Expected Int")

    # Selection sort algorithm
    n = len(list3)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if list3[j] < list3[min_index]:
                min_index = j
        list3[i], list3[min_index] = list3[min_index], list3[i]

    return list3
