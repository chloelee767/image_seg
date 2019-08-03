from pathlib import Path

INTERNSHIPDIR = Path('/home/chloe/Documents/internship')
RESULTSDIR = INTERNSHIPDIR / 'github/segmentation-results'

CONFIGDIR = RESULTSDIR / 'model_configs' # configs and splits go here
WEIGHTSDIR = RESULTSDIR / 'model_weights'

LOGDIR = RESULTSDIR / 'logs' # csv logs
PREDDIR = RESULTSDIR / 'predictions'
COMMONDIR = RESULTSDIR/'common' #DRIVEDIR / 'data'

DATADIR = INTERNSHIPDIR / 'lst_data'

IMGDIR = DATADIR /'images'
MASKDIR = DATADIR / 'masks'
