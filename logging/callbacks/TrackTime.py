from keras.callbacks import Callback
import time
class TrackTime(Callback):
    def __init__(self):
        super().__init__()
        
    def on_epoch_begin(self,epoch,logs=None):
        self.epoch_start = time.time()
        
    def on_epoch_end(self,epoch,logs=None):
        epoch_time = time.time() - self.epoch_start
        if logs:
            logs['epoch_time'] = epoch_time
        super().on_epoch_end(epoch,logs)
