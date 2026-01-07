from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(100, 10)) == 100


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(150, 1) == [150]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)
    assert result == [5, 5, 5, 5, 6, 6]

    result_diff = split_integer(17, 4)
    assert result_diff == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # If we split 2 into 5 parts, we need three 0s and two 1s
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
    # If we split 0 into 3 parts, we get three 0s
    assert split_integer(0, 3) == [0, 0, 0]
