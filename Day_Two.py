# Day 2: Gift shop

filename = "Input_day2.txt"


def read_file_to_list():
    with open(filename, "r") as file:
        for line in file:
            return line


def split_input_into_list(input):
    input_list = input.split(",")
    return input_list


def validate_id(id):
    id_map = map(int, str(id))
    id_list = list(id_map)
    if len(id_list) == 1:
        return True  #Number is automatically valid, because its a single diget
    if len(id_list) % 2 == 1: # Odd number cannot be invalid
        return True
    mid_point = len(id_list) // 2
    first_half = id_list[:mid_point]
    second_half = id_list[mid_point:]
    first_number = int("".join(str(x) for x in first_half))
    second_number = int("".join(str(x) for x in second_half))
    if first_number == second_number:
        print(f"is invalid {id}")
        return False
    return True


def find_invalid_id_in_range(lower, upper):
    invalid_sum = 0
    while lower <= upper:
        if not validate_id(lower):
            invalid_sum += lower
        lower += 1
    return invalid_sum


def main():
    print("main()")
    input = read_file_to_list()
    list_of_ids = split_input_into_list(input)
    total_invalid_ids = 0
    for id in list_of_ids:
        id_range = id.split("-")
        total_invalid_ids += find_invalid_id_in_range(int(id_range[0]), int(id_range[1]))

    print(f"Total number of invalid ids is {total_invalid_ids}")


main()
