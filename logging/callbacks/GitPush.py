from keras.callbacks import Callback

class GitPush(Callback):
    def __init__(self,git_repo):
        super().__init__()
        self.repo = git_repo
        
    def on_epoch_end(self,epoch,logs=None):
        self.repo.commit_and_push('Epoch ' + str(epoch))
