import yaml
from faker import Faker
from tqdm import trange

from rtofdata.config import template_dir
from rtofdata.fake import generators
from rtofdata.fake.generators import get_date_or_delta
from rtofdata.specification.parser import parse_specification

faker = Faker()


def generate_records(datastore, spec, context, record_name, config, progress=False):
    local_context = config.get('context', {})
    if "start" in local_context:
        local_context['start'] = get_date_or_delta(local_context.get("start"), context['date'])
    if "end" in local_context:
        local_context['end'] = get_date_or_delta(local_context.get("end"), context['date'])

    context = {**context, **local_context}

    if "seed" in context:
        Faker.seed(context["seed"])
        del context["seed"]

    my_range = trange if progress else range

    for ix in my_range(0, config.get("num", 1)):
        if faker.random.random() > config.get('probability', 1.0):
            continue
        record_context = {**context, "date": faker.date_between(context['start'], context['end'])}

        id, record = generate_record(spec, record_context, record_name, config, faker, ix)
        datastore.setdefault(record_name, {})[id] = record

        if "parent_id" not in record_context:
            record_context["parent_id"] = id

        for sub_record_name, sub_config in config.get('records', {}).items():
            generate_records(datastore, spec, record_context, sub_record_name, sub_config)


def generate_record(spec, context, record_name, config, faker, ix):
    record_spec = spec.record_by_id(record_name)
    record = {}

    id = []
    for f in record_spec.fields:
        field_config = config.get("fields", {}).get(f.id, {})

        validators = [v['description'] for v in f.validation]
        probability = 1.0 if "required(True)" in validators else 0.5
        probability = field_config.get("probability", probability)

        if faker.random.random() > probability:
            continue

        if f.foreign_keys:
            gen = lambda *args, **kwargs: context['parent_id']
        elif "method" in field_config:
            gen = getattr(generators, field_config['method'])
        else:
            gen = getattr(generators, f.type.id)

        args = {}
        if "args" in field_config:
            args = field_config.get('args', {})

        record[f.id] = gen(faker, context, field=f, record=record, **args)
        if f.primary_key:
            id.append(record[f.id])

    return id[0] if len(id) < 2 else tuple(id), record


def create_all_data(spec=None, config_file=None, num=None, progress=False):
    if not spec:
        spec = parse_specification()

    if config_file is None:
        config_file = template_dir / "samples/small.yml"

    with open(config_file, "rt") as file:
        gen_spec = yaml.safe_load(file)

    context = gen_spec.get('context', {})
    records = gen_spec.get('records', {})

    datastore = {}
    for record_name, config in records.items():
        if num:
            config["num"] = num
        generate_records(datastore, spec, context, record_name, config, progress=progress)

    return datastore