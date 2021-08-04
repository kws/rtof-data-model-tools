from faker import Faker
from numpy import random
from numpy.core.fromnumeric import transpose
from numpy.random.mtrand import rand
import pandas as pd
from datetime import date, datetime
import numpy as np
from pandas.core import base
import yaml

fake = Faker()


def create_person_data(x):
    person_data = {}
    with open("data/categories/gender.yml") as f:
        genders = yaml.load(f.read())
    with open ("data/records/person.yml") as f:
        date_of_birth = yaml.load(f.read())
        date_of_birth_start = date_of_birth['fields']['date_of_birth']['args']['start_date']
        date_of_birth_end = date_of_birth['fields']['date_of_birth']['args']['end_date']
    for i in range(0, x):
        person_data[i] = {}
        person_data[i]['NiNo'] = fake.bothify('?? ######')
        person_data[i]['date_of_birth'] = fake.date_between(start_date = date_of_birth_start, end_date = date_of_birth_end)
        person_data[i]['gender'] = np.random.choice(genders)
        person_data[i]['dispersal_area'] = fake.postcode()
        person_data[i]['date_started_service'] = fake.date_this_month(before_today=False, after_today=True)
    return person_data

person_fake = create_person_data(10)
person_df = pd.DataFrame.from_dict(person_fake) 
print(transpose(person_df))

def create_baseline_data(x):
    baseline_data ={}
    with open("data/categories/nationality.yml") as f:
        nationalities = yaml.load(f.read())
        nationalities = [n['value'] for n in nationalities]
    with open("data/categories/language_level_on_entry.yml") as f:
        language_level = yaml.load(f.read())  
    with open("data/categories/transgender.yml") as f:
        gender_follow_up = yaml.load(f.read())  
    with open("data/categories/living_status.yml") as f:
        living_status = yaml.load(f.read())
    with open("data/categories/current_family_composition.yml") as f:
        current_family_composition = yaml.load(f.read())
    with open("data/records/baseline.yml") as f:
        arrived_uk = yaml.load(f.read())
        arrived_uk_start = arrived_uk['fields']['date_arrived_in_uk']['args']['start_date']
        arrived_uk_end = arrived_uk['fields']['date_arrived_in_uk']['args']['end_date']
    with open("data/records/baseline.yml") as f:
        asylum_granted = yaml.load(f.read())
        asylum_granted_start = asylum_granted['fields']['date_asylum_status_granted']['args']['start_date']
        asylum_granted_end = asylum_granted['fields']['date_asylum_status_granted']['args']['end_date']
    with open("data/categories/highest_qualification_achieved.yml") as f:
        highest_qualification_achieved = yaml.load(f.read())
    with open("data/categories/employed_in_home_country.yml") as f:
        employed_in_home_country = yaml.load(f.read())
    with open("data/categories/economic_status.yml") as f:
        economic_status = yaml.load(f.read())
    with open("data/categories/housing_baseline_accommodation.yml") as f:
        housing_baseline_accommodation = yaml.load(f.read())
    for i in range(0, x):
        baseline_data[i] = {}
        baseline_data[i]['person_ni_number'] = fake.bothify('?? ######')
        baseline_data[i]['Nationality'] = np.random.choice(nationalities)
        baseline_data[i]['language_level_on_entry'] = np.random.choice(language_level)  
        baseline_data[i]['gender_follow_up'] = np.random.choice(gender_follow_up)
        baseline_data[i]['living_status'] = np.random.choice(living_status)
        baseline_data[i]['current_family_composition'] = np.random.choice(current_family_composition)
        baseline_data[i]['date_arrived_in_uk'] = fake.date_between(start_date = arrived_uk_start, end_date = arrived_uk_end)
        baseline_data[i]['date_asylum_status_granted'] = fake.date_between(start_date = asylum_granted_start, end_date = asylum_granted_end)
        baseline_data[i]['highest_qualification_achieved'] = np.random.choice(highest_qualification_achieved)
        baseline_data[i]['employed_in_home_country'] = np.random.choice(employed_in_home_country)
        baseline_data[i]['occupation_type'] = fake.words(2)
        baseline_data[i]['occupation_sector'] = fake.words(2)
        baseline_data[i]['occupation_goal'] = fake.words(2)
        baseline_data[i]['economic_status'] = np.random.choice(economic_status)
        baseline_data[i]['housing_baseline_accommodation'] = np.random.choice(housing_baseline_accommodation)
    return baseline_data

baseline_fake = create_baseline_data(10)
baseline_df = pd.DataFrame.from_dict(baseline_fake)
print(transpose(baseline_df))

def create_date_last_seen_data(x):
    date_last_seen_data = {}
    for i in range(0, x):
        date_last_seen_data[i] = {}
        date_last_seen_data[i]['unqiue_id'] = fake.bothify('?? ######')
        date_last_seen_data[i]['date_last_seen'] = fake.date_between()
    return date_last_seen_data

date_last_seen_fake = create_date_last_seen_data(20)
date_last_seen_df = pd.DataFrame.from_dict(date_last_seen_fake)
print(transpose(date_last_seen_df))

def create_employment_entry_data(x):
    employment_entry__data = {}
    with open("data/categories/employment_entry_outcome_type.yml") as f:
        employment_entry_outcome_type = yaml.load(f.read())
    with open("data/categories/employment_entry_details.yml") as f:
        employment_entry_details = yaml.load(f.read())
    for i in range(0, x):
        employment_entry__data[i] = {}
        employment_entry__data[i]['unique_id'] = fake.bothify('?? ######')
        employment_entry__data[i]['employment_entry_outcome_type'] = np.random.choice(employment_entry_outcome_type)
        employment_entry__data[i]['date_employment_entry'] = fake.date_between()
        employment_entry__data[i]['employment_entry_details'] = np.random.choice(employment_entry_details)
        employment_entry__data[i]['employment_entry_occupation'] = fake.words(2)
        employment_entry__data[i]['employment_entry_sector'] = fake.words(2)
    return employment_entry__data

employment_entry_fake = create_employment_entry_data(10)
employment_entry_df = pd.DataFrame.from_dict(employment_entry_fake)
print(transpose(employment_entry_df))

def create_employment_intermediate_data(x):
    employment_intermediate_data = {}
    with open("data/records/employment_intermediate.yml") as f:
        intermediate_employment_outcome = yaml.load(f.read())
        intermediate_employment_outcome_start = intermediate_employment_outcome['fields']['date_intermediate_employment_outcome']['args']['start_date']
        intermediate_employment_outcome_end = intermediate_employment_outcome['fields']['date_intermediate_employment_outcome']['args']['end_date']
    with open("data/categories/intermediate_employment_outcome_type") as f:
        intermediate_employment_outcome_type = yaml.load(f.read())
    for i in range(0,x):
        employment_intermediate_data[i] = {}
        employment_intermediate_data[i]['unique_id'] = fake.bothify('?? ######')
        employment_intermediate_data[i]['date_intermediate_employment_outcome'] = fake.date_between(start_date = intermediate_employment_outcome_start, end_date= intermediate_employment_outcome_end)
        employment_intermediate_data[i]['intermediate_employment_outcome_type'] = random.choice(intermediate_employment_outcome_type, 3)
    return employment_intermediate_data

employment_intermediate_fake = create_employment_intermediate_data(10)
employment_intermedate_df = pd.DataFrame.from_dict(employment_intermediate_fake)
print(transpose(employment_intermedate_df))

def create_employment_sustain_data(x):
    employment_sustain_data = {}
    with open("data/records/employment_sustain.yml") as f:
        employment_sustain_date = yaml.load(f.read())
        employment_sustain_date_start = employment_sustain_date['fields']['employment_sustainment_date']['args']['start_date']
        employment_sustain_date_end = employment_sustain_date['fields']['employment_sustainment_date']['args']['end_date']
    for i in range(0, x):
        employment_sustain_data[i] = {}
        employment_sustain_data[i]['unique_id'] = fake.bothify('?? ######')
        employment_sustain_data[i]['employment_sustain_date'] = fake.date_between(start_date= employment_sustain_date_start, end_date = employment_sustain_date_end)
    return employment_sustain_data
employment_sustain_fake = create_employment_sustain_data(10)
employment_sustain_df = pd.DataFrame.from_dict(employment_sustain_fake)
print(transpose(employment_sustain_df))
