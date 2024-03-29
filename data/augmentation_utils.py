from ..preproc.augmentation import num_aug, num_tta

def make_train_list(lst,num_aug = num_aug):
    train_list = lst.copy()
    n = len(train_list)
    for i in range(n):
        for j in range(num_aug):
            train_list.append(f'{train_list[i]}_aug{j}')
    return train_list

def make_test_list(lst,num_tta=num_tta):
    test_list = lst.copy()
    n = len(test_list)
    for i in range(n):
        for j in range(num_tta):
            test_list.append(f'{test_list[i]}_tta{j}')
    return test_list
