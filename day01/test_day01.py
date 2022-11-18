import day01_01
import day01_02


def test_multiply_two_numbers_which_sum_is_2020():
    assert (
        day01_01.multiply_two_numbers_which_sum_is_2020("example_input.txt") == 514579
    )


def test_multiply_three_numbers_which_sum_is_2020():
    assert (
        day01_02.multiply_three_numbers_which_sum_is_2020("example_input.txt")
        == 241861950
    )
