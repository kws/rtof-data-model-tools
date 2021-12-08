import tablib
from rtofdata.parser import Parser
from tests.conftest import quick_spec


def test_null_headers():

    data = tablib.Dataset(
        ['A', 'User', 'M', 'Test', 'Random'],
        ['B', 'User', 'M', 'Test', 'Random'],
        headers=['first_name', 'last_name', 'gender', None, 'something_else']
    )

    spec = quick_spec({"person": (
        ("firstname", "string"),
        ("lastname", "string"),
        ("gender", "string"),
    )})

    parser = Parser(spec)
    events = parser.dataset_to_events(data)
    assert len(events) == 6

