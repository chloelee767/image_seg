import itertools
from ..configs.default import *
from .get_files import *

def train_val_split(splits,valid_index):
    train_list_2d = splits[:valid_index]
    train_list_2d.extend(splits[valid_index+1:])
    train_list = list(itertools.chain.from_iterable(train_list_2d))
    valid_list = splits[valid_index]
    return train_list,valid_list

import json

def open_split(name,folder=CONFIGDIR):
    with open(Path(folder)/name) as f:
        filedict = json.load(f)
    return filedict['split'] , filedict['val_patients']

def create_split(n_splits=5,name,folder=CONFIGDIR):
    from random import sample, shuffle

    full_train_list = get_full_train_list()
    full_train_patients = get_full_train_patients()
    dir_map = get_directory_mapping()

    # do train/val split
    # pick 5 different patients at random to add to validation set
    val_patients = sample(full_train_patients,n_splits)

    train_list = full_train_list.copy()
    split_size = len(train_list) // n_splits
    splits = []
    for patient in val_patients:
        imgs = dir_map[patient[0]][patient[1]]
        splits.append(imgs)
        for img in imgs:
            train_list.remove(img)

    # add rest of patients
    shuffle(train_list)
    pos = 0
    for i,lst in enumerate(splits):
        needed = split_size - len(lst)
        splits[i].extend(train_list[pos:pos+needed])
        pos += needed
    splits[n_splits-1].extend(train_list[pos:])

    for split in splits:
        print(len(split))
    
    # Save splits
    with open(Path(folder) / name,'w+') as f:
        json.dump({
            'val_patients' : val_patients,
            'split' : splits,
        },f,indent=4)
    
    return splits, val_patients
