def get_lr_metric(optimizer):
    def lr(y_true, y_pred):
        return optimizer.lr
    return lr        

