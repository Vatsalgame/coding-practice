def print_combos(nested_list):
    for element in nested_list[0]:
        print_combo_helper(element, nested_list[1:])


def print_combo_helper(element, sub_list):
    if sub_list:
        for item in sub_list[0]:
            print(element)
            print_combo_helper(item, sub_list[1:])


if __name__ == "__main__":
    list_of_lists = [['a', 'b'], ['1', '2'], ['+', '-']]
    print_combos(list_of_lists)