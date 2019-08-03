from keras import optimizers

def make_optimizer(name,args):
    opt = getattr(optimizers,name)(**args)
    return opt
