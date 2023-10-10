def reverse_sort_dictionary(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda x: x[0], reverse=True)
    result_list = [(name, phone) for name, (phone, _) in sorted_items]
    return result_list
