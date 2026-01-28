def find(search_list, value):
    list_length = len(search_list)
    if list_length == 1 and search_list[0] != value or list_length == 0:
        raise ValueError("value not in array")
    
    mid_index = list_length // 2
    print(mid_index)
    if search_list[mid_index] == value:
        return mid_index
    if search_list[mid_index] < value:
        return mid_index + find(search_list[mid_index:], value)
    else:
        return find(search_list[:mid_index], value)
