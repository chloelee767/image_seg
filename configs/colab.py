from pathlib import Path

DRIVEDIR = Path('/content/drive/My Drive/unet_files')
GITDIR = Path('/content/segmentation-results')

CONFIGDIR = GITDIR / 'model_configs' # configs and splits go here
GIT_WEIGHTSDIR = GITDIR / 'model_weights'
DRIVE_WEIGHTSDIR = DRIVEDIR / 'model_weights'
WEIGHTSDIR = DRIVE_WEIGHTSDIR

LOGDIR = GITDIR / 'logs' # csv logs
PREDDIR = GITDIR / 'predictions'
COMMONDIR = GITDIR/'common' #DRIVEDIR / 'data'

DATADIR = Path('/content/lst_data')

IMGDIR = DATADIR /'images'
MASKDIR = DATADIR / 'masks'
