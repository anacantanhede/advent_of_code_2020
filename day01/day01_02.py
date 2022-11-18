def multiply_three_numbers_which_sum_is_2020(input_file):
    with open(input_file) as f:
        int_list = [int(i) for i in f.read().split()]

    for index1, num1 in enumerate(int_list):
        for index2, num2 in enumerate(int_list[index1 + 1 : len(int_list) - 1]):
            for index3, num3 in enumerate(int_list[index2 + 1 : len(int_list) - 1]):
                if num1 + num2 + num3 == 2020:
                    # print(f"{num1}, {num2}, {num1+num2}, {num1*num2}")
                    return num1 * num2 * num3


if __name__ == "__main__":
    print(multiply_three_numbers_which_sum_is_2020("input.txt"))
