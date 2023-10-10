def reverse_sort_dictionary(input_dict):
    result_list = []
    for name, (phone, _) in sorted(input_dict.items(), key=lambda x: x[0], reverse=True):
        result_list.append((name, phone))
    return result_list
