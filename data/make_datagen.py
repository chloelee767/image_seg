from . import DataGen
from ..preproc.normalisation import minmax_norm

def make_train_datagen(lst,**datagen_args):
    return DataGen(lst,shuffle=True,preproc=minmax_norm,**datagen_args)

def make_test_datagen(lst,**datagen_args):
    return DataGen(lst,shuffle=False,preproc=minmax_norm,**datagen_args)

