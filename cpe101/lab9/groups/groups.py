def groups_of_3(in_list):
    new_list = []
    list_3 = []
    for i in range(len(in_list)):
        list_3.append(in_list[i])
        if (i + 1) % 3 == 0 or i == len(in_list) - 1:
            new_list.append(list_3)
            list_3 = []
    return new_list



