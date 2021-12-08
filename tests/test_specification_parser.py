from pathlib import Path
from rtofdata.specification.parser import SpecificationParser
from tests.conftest import standard_datatypes


class TestSpecificationParser:

    def test_parse_records(self):
        records = SpecificationParser.parse_records(
            standard_datatypes, [], [], [Path(__file__).parent / "files/spec/sample1/records/table1.yml"]
        )

