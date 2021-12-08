from rtofdata.datasource.in_memory import InMemoryDataSource
from rtofdata.parser.parser import DataEvent
from tests.conftest import quick_spec


class TestInMemoryDatasource:

    def test_basic_to_eventstream(self):
        spec = quick_spec({"person": (
            ("unique_id", "string", True),
            ("year_of_birth", "int"),
            ("gender", "string"),
        )})

        events = [
            _gen_event(spec, "person", "year_of_birth", "1989", unique_id="DP-14"),
            _gen_event(spec, "person", "gender", "Woman", unique_id="DP-14"),
        ]

        ds = InMemoryDataSource(spec)
        for e in events:
            ds.update(e)

        expected_result = dict(unique_id="DP-14", year_of_birth="1989", gender="Woman")
        actual_result = ds.get_single_record("person", "DP-14")._asdict()
        assert actual_result == actual_result | expected_result

        ds.update(_gen_event(spec, "person", "gender", "Man", unique_id="DP-14"))

        expected_result = dict(unique_id="DP-14", year_of_birth="1989", gender="Man")
        actual_result = ds.get_single_record("person", "DP-14")._asdict()

        assert actual_result == actual_result | expected_result


def _gen_event(spec, record_id, field_id, value, **primary_keys):
    pk = spec.record_by_id(record_id).get_key(**primary_keys)
    return DataEvent(
        record=record_id,
        field=field_id,
        value=value,
        primary_key=pk
    )


