from albumentations import *

num_aug = 5

training_aug = Compose([
    Blur(p=0.6,blur_limit=4),
    RandomBrightnessContrast(p=0.8),
    HueSaturationValue(p=0.6, val_shift_limit=10, hue_shift_limit=5),
    CLAHE(p=0.2),
    GridDistortion(border_mode=0),
    RandomRotate90(),
    HorizontalFlip(),
    RandomScale()
])

# rotate 90, 180, 270 and flip
tta = [
    Rotate((90,90),p=1),
    Rotate((180,180),p=1),
    Rotate((270,270),p=1),
    HorizontalFlip(p=1)
]
num_tta = len(tta)

import imageio
from ...configs.default import *

def run_training_aug(full_train_list):
    for filename in full_train_list:
        img = imageio.imread(IMGDIR/f'{filename}.jpg')
        mask = imageio.imread(MASKDIR/f'{filename}.png')
        for i in range(num_aug):
            aug = training_aug(image=img,mask=mask)
            imageio.imwrite(IMGDIR/f'{filename}_aug{i}.jpg',aug['image'])
            imageio.imwrite(MASKDIR/f'{filename}_aug{i}.png',aug['mask'])
    
def run_tta(lst):
    for filename in lst:
        img = imageio.imread(IMGDIR/f'{filename}.jpg')
        mask = imageio.imread(MASKDIR/f'{filename}.png')
        for i in range(num_tta):
            aug = tta[i](image=img,mask=mask)
            imageio.imwrite(IMGDIR/f'{filename}_tta{i}.jpg',aug['image'])
            imageio.imwrite(MASKDIR/f'{filename}_tta{i}.png',aug['mask'])
