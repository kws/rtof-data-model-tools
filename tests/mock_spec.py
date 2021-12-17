from rtofdata.specification import data as rtofdata


def _gen_field(field_id, field_type, **kwargs):
    return rtofdata.Field(id=field_id, name=field_id, description=field_id, type=field_type, **kwargs)


def mock_specification():
    records = [
        rtofdata.Record(id="person", description="Person", fields=[
            _gen_field("unique_id", "integer", primary_key=True),
            _gen_field("year_of_birth", "integer"),
            _gen_field("gender", "string"),
            _gen_field("dispersal_area", "string"),
            _gen_field("date_started_service", "string"),
        ]),
    ]
    categories = []
    flows = []
    validators = []
    datatypes = [
        rtofdata.Datatype(id="string",
                          description="A string of Unicode characters as defined by the JSON Schema `string` type."),
        rtofdata.Datatype(id="integer", description="An integer as defined by the JSON Schema `integer` type."),
    ]

    return rtofdata.Specification(records=records, dimensions=categories, flows=flows, validators=validators,
                                  datatypes=datatypes)
