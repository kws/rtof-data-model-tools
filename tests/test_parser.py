import tablib

from rtofdata.parser import Parser
from tests.mock_spec import mock_specification


def test_null_headers():
    spec = mock_specification()

    parser = Parser(spec)

    data = tablib.Dataset(*[
        ['A', 'User', 'M', 'Test', 'Random'],
        ['B', 'User', 'M', 'Test', 'Random'],
    ], headers=['first_name	', 'last_name', 'gender', None, 'something_else'])

    parser.dataset_to_events(data)