from collections.abc import Mapping, Iterable
from typing import Iterator, Dict, List, Tuple, Union

from rtofdata.specification import data as rtofdata

standard_datatypes = [
    rtofdata.Datatype(id='int'),
    rtofdata.Datatype(id='string'),
    rtofdata.Datatype(id='float'),
]


def quick_spec(spec: Dict[str, Iterable[Union[
    Tuple[str, str],
    Tuple[str, str, bool],
    Tuple[str, str, bool, bool],
]]],
               datatypes: Iterable[rtofdata.Datatype] = None) -> rtofdata.Specification:
    if datatypes is None:
        datatypes = standard_datatypes

    dt = {d.id: d for d in datatypes}

    records = []
    for record_id, fields in spec.items():
        record = rtofdata.Record(
            id=record_id,
            fields=[rtofdata.Field(id=f[0], name=f[0], type=dt[f[1]],
                                   primary_key=f[2] if len(f) > 2 else False) for f in fields],
        )
        records.append(record)

    return rtofdata.Specification(datatypes=datatypes, records=records)
