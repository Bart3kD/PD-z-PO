import pytest
from main import approximate_sqrt
from main import main


def test_returns_float() -> None:
    actual = approximate_sqrt(4, 2)
    assert isinstance(actual, float)

def test_returns_2() -> None:
    actual = approximate_sqrt(4, 2)
    assert actual == 2.0

def test_returns_0() -> None:
    actual = approximate_sqrt(0, 2)
    assert actual == 0

def test_returns_0_for_number_less_than_zero() -> None:
    actual = approximate_sqrt(-2, 2)
    assert actual == 0

def test_returns_string_error_for_string_number_less_than_zero() -> None:
    actual = approximate_sqrt('4', 2)
    assert isinstance(actual, str)

def test_returns_string_error_for_wrong_precision() -> None:
    actual = approximate_sqrt(4, '2')
    assert isinstance(actual, str)


@pytest.fixture
def input_pos1(monkeypatch):
    user_input = iter(['4', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(user_input))

@pytest.fixture
def input_pos1_res():
    return 2.0

def test_prints_pos_input1(capsys, input_pos1, input_pos1_res) -> None:
    main()
    assert (input_pos1_res == float(capsys.readouterr().out))