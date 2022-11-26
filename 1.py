def replacing_non_lists_to_lists(list_of_lists: list):
    """ we check list_of_lists on non list elements and change it
    [
        [False, True],
        0,
        ['first', 'second', 'third']
    ]
    =
    [
        [False, True],
        [0],
        ['first', 'second', 'third']
    ]
    """
    for index_and_nested_list in enumerate(list_of_lists):
        if not isinstance(index_and_nested_list[1], list):
            list_of_lists[index_and_nested_list[0]] = [index_and_nested_list[1]]
    return list_of_lists


def how_many_numbers_can_be_encoded(list_of_lists: list):
    """ we find the maximum number of numbers that we can encode
    [[1,2,3],
    [1,2,3],
    [1,2,3]] max count of number ==> 3*3*3 = 27
    """
    possible_number_of_numbers = 1
    for nested_list in list_of_lists:
        possible_number_of_numbers *= len(nested_list)
    return possible_number_of_numbers


def cut_off_the_lap_of_list(possible_number_of_numbers: int, variant: int):
    """ cut off all the extra circles that do not affect the result
    111 = [1,1,1]
    """
    if possible_number_of_numbers < variant:
        variant = variant % possible_number_of_numbers
    return variant


def get_variant_numbers_in_list(variant: int):
    return [int(x) for x in str(variant)]


def add_zeros_to_empty_fields(len_number_list: int, len_list_of_lists: int, number_list: list):
    """
    list_of_list = [[1,2,3],  number_list = [1,2] after this func number_list = [1,2,0]
                    [1,2,3],
                    [1,2,3]]
    """
    if len_number_list < len_list_of_lists:
        for i in range(len_list_of_lists - len_number_list):
            number_list.insert(len_number_list, 0)
    return number_list


def create_valid_list_of_numbers(list_of_lists: list, number_list: list):
    """
    list_of_list = [[1,2,3],  number_list = [1,5,0] after this func number_list = [2,2,0]
                    [1,2,3],  5 > len(list_of_lists[1]) ==> 5 % 3 = 2 = remainder | 5 // 3 = 1 = without_a_remainder
                    [1,2,3]]         [1 + without_a_remainder, remainder, 0]
    """
    for nested_list, index_and_number in zip(list_of_lists, enumerate(number_list)):
        if index_and_number[0] == 0:
            if index_and_number[1] > len(nested_list):
                without_a_remainder = index_and_number[1] // len(nested_list)
                remainder = index_and_number[1] % len(nested_list)
                number_list[index_and_number[0]] = remainder
                number_list[index_and_number[0] + 1] = number_list[index_and_number[0] + 1] + without_a_remainder
        else:
            if index_and_number[1] >= len(nested_list):
                without_a_remainder = index_and_number[1] // len(nested_list)
                remainder = index_and_number[1] % len(nested_list)
                number_list[index_and_number[0]] = remainder
                number_list[index_and_number[0] + 1] = number_list[index_and_number[0] + 1] + without_a_remainder
    return number_list


def coding(list_of_lists: list, number_list: list):
    """
    list_of_list = [[1,2,3],  variant = 12              list_of_list[0][number_list[0]] = 1
                    [1,2,3],  number_list = [0,1,2]     list_of_list[1][number_list[1]] = 2
                    [1,2,3]]  result = [1,2,2]          list_of_list[2][number_list[2]] = 2
    """
    result = []
    for nested_list, index_and_number in zip(list_of_lists, enumerate(number_list)):
        if index_and_number[0] == 0:
            if index_and_number[1] > len(nested_list):
                result.append(nested_list[index_and_number[1] - 1])
            else:
                result.append(nested_list[index_and_number[1] - 1])
        else:
            if index_and_number[1] > len(nested_list):
                result.append(nested_list[index_and_number[1]])
            else:
                result.append(nested_list[index_and_number[1]])
    result.reverse()
    return result


def find_special_massive_of_number(list_of_lists: list, variant: int) -> list:
    list_of_lists = replacing_non_lists_to_lists(list_of_lists)
    possible_number_of_numbers = how_many_numbers_can_be_encoded(list_of_lists)
    variant = cut_off_the_lap_of_list(possible_number_of_numbers, variant)
    number_list = get_variant_numbers_in_list(variant)
    number_list.reverse()
    list_of_lists.reverse()
    len_number_list = len(number_list)
    len_list_of_lists = len(list_of_lists)
    add_zeros_to_empty_fields(len_number_list, len_list_of_lists, number_list)
    number_list = create_valid_list_of_numbers(list_of_lists, number_list)
    result = coding(list_of_lists, number_list)
    return result


assert find_special_massive_of_number([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
], 1) == [0, 0, 0]
assert find_special_massive_of_number([
    [0, 1, 2],
    [0, 1, 2, 3, 4, 5, 6, ],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
], 2) == [0, 0, 1]

assert find_special_massive_of_number([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
], 138) == [1, 3, 7]

assert find_special_massive_of_number([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
], 538) == [5, 3, 7]

assert find_special_massive_of_number([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
], 1012) == [0, 1, 1]
assert find_special_massive_of_number(
    [
        [False, True],
        0,
        ['first', 'second', 'third']
    ], 4) == [True, 0, 'first']
assert find_special_massive_of_number(
    [
        [False, True],
        0,
        ['first', 'second', 'third']
    ], 9) == [False, 0, 'third']

assert find_special_massive_of_number(
    [
        [False, True],
        0,
        ['first', 'second', 'third']
    ], 13) == [False, 0, 'first']

assert find_special_massive_of_number([
    [0, 1, 2, 8, 9],
    [0, 1, 2, 3, 8, 9],
    [0, 1, 7, 8, 9],
], 10) == [0, 1, 9]

assert find_special_massive_of_number(
    [
        0,
        [False, True],
        ['first', 'second', 'third']
    ], 13) == [0, False, 'first']

assert find_special_massive_of_number(
    [
        [False, True],
        ['first', 'second', 'third'],
        0,
    ], 13) == [False, 'first', 0]

assert find_special_massive_of_number(
    [
        [False, True],
        0,
        0,
    ], 13) == [False, 0, 0]
