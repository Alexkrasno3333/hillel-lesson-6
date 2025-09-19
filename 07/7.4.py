def common_elements():
    first_list = range(0, 100)
    first_list = (x for x in first_list if x % 3 == 0)
    first_list = set(first_list)
    second_list = range(0,100)
    second_list = (x for x in second_list if x % 5 == 0)
    second_list = set(second_list)
    sum = first_list & second_list
    return sum

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
