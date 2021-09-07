from tablib import Dataset, Databook


def parse(file):
    with open(file, 'rb') as fh:
        imported_data = Databook().load(fh, 'xlsx')

    for ds in imported_data.sheets():
        print(ds.headers)