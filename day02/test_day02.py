import day02_01


def test_password_is_valid():
    assert day02_01.password_is_valid("1-3 a", "") is False
    assert day02_01.password_is_valid("1-3 a", "a") is True
    assert day02_01.password_is_valid("1-3 a", "aaa") is True
    assert day02_01.password_is_valid("1-3 a", "aaaa") is False
    assert day02_01.password_is_valid("1-3 a", "baac") is True
    assert day02_01.password_is_valid("1-3 a", "bbccd") is False
    assert day02_01.count_valid_passwords("example_input.txt") == 2
