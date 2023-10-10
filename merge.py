def merge_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")

    if not all(isinstance(element, int) for sublist in [list1, list2] for element in sublist):
        raise TypeError("All elements in the lists must be integers")

    merged_list = list1 + list2

    for i in range(len(merged_list)):
        for j in range(0, len(merged_list) - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    return merged_list
