import json
from ..configs.default import COMMONDIR

def get_full_train_list():
    with open(COMMONDIR/'train_list.json') as f:
        full_train_list = json.load(f)
    return full_train_list

def get_test_list():
    with open(COMMONDIR/'test_list.json') as f:
        test_list = json.load(f)
    return test_list

def get_directory_mapping():
    with open(COMMONDIR/'directory_mapping.json') as f:
        dir_map = json.load(f)
    return dir_map

def get_filename_mapping():    
    with open(COMMONDIR/'filename_mapping.json') as f:
        filename_map = json.load(f)
    return filename_map

def get_full_train_patients(full_train_list=None,filename_map=None):
    if not full_train_list:
        full_train_list = get_full_train_list()
    if not filename_map:
        filename_map = get_filename_mapping()

    full_train_patients = set() 
    for filename in full_train_list:
        info = filename_map[filename]
        full_train_patients.add((info['invasive_str'],info['patient']))

    return full_train_patients
