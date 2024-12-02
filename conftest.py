import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--input", action='store', default='default_value', help='input value for testing',
    )

@pytest.fixture
def get_console_input(request):
    return request.config.getoption("--input")

