from text import name_case, initials
import pytest


def test_name_case_all_upper_case():
    actual = 'JONAS JONAITIS'
    expected = 'Jonas Jonaitis'
    assert name_case(actual) == expected

def test_name_case_all_lower_case():
    actual = 'jonas jonaitis'
    expected = 'Jonas Jonaitis'
    assert name_case(actual) == expected

def test_name_case_more_than_two_words():
    actual = 'jonas jonys jonaitis'
    expected = 'Jonas Jonys Jonaitis'
    assert name_case(actual) == expected

def test_name_case_dash_between_words():
    actual = 'jonas jonys-jonaitis'
    expected = "Jonas Jonys-Jonaitis"
    assert name_case(actual) == expected

def test_initials_lower_case():
    actual = "jonas jonaitis"
    expected = "J.J."
    assert initials(actual) == expected


# To run one test: pytest test_file.py::test_name_case_dash_between_words
# To run several tests: pytest test_file.py::test_name_case_dash_between_words test_file.py::test_initials_lower_case

def test_name_case_with_console_input(get_console_input):
    expected = "Jonas Jonaitis"
    assert name_case(get_console_input) == expected

# To run the test with console input: pytest test_file.py::test_name_case_with_console_input --input "jonas jonaitis"



@pytest.mark.parametrize('actual, expected',[('jonas','Jonas'),('JONAS JONAITIS','Jonas Jonaitis'),('jonas jonys-jonaitis','Jonas Jonys-Jonaitis')])
def test_parameterized_name_case(actual, expected):
    assert name_case(actual) == expected

# To run parameterized test with several input-output pairs: pytest test_file.py::test_parameterized_name_case