from keras.callbacks import Callback

class TestOnEpoch(Callback):
    def __init__(self,test_datagen):
        self.datagen = test_datagen
        super().__init__()
        
    def on_epoch_end(self,epoch,logs=None):
        if logs:
            results = self.model.evaluate_generator(self.datagen)
            for metric,result in zip(self.model.metrics_names,results):
                if metric=='lr':
                    continue
                logs[f'test_{metric}'] = result
                
        super().on_epoch_end(epoch,logs)
