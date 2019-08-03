from keras.utils import Sequence
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from ..configs.default import IMGDIR, MASKDIR
from random import shuffle
import numpy as np

class DataGen(Sequence):
    def __init__(self, ids, 
                 shuffle=False,preproc=None,
                 batch_size=16, img_shape=(512, 512, 3),
                 imgs_dir = IMGDIR, 
                 masks_dir = MASKDIR, 
                 imgs_ext = 'jpg', 
                 masks_ext = 'png', 
                 masks_suffix = '',
                 ):
        """
        Args:
            ids (list[str]): Filenames of images (without extension).
            imgs_dir (Path): Path to images dir.
            masks_dir (Path): Path to masks dir.
            imgs_ext (str): e.g. jpg
            masks_ext (str): e.g. png
            masks_suffix (str):
            batch_size (int):
            img_shape ((height, width, channels)): Image shape to resize to.
            shuffle (boolean): Whether to shuffle data after each epoch.
            aug (func): Optional augmentation function wrapper that augments a
                single image.
        """
        self.ids = ids
        self.imgs_dir = imgs_dir
        self.masks_dir = masks_dir
        self.imgs_ext = imgs_ext
        self.masks_ext = masks_ext
        self.masks_suffix = masks_suffix
        self.batch_size = batch_size
        self.img_shape = img_shape
        self.shuffle = shuffle
        self.preproc = preproc
        
        self.on_epoch_end()
        
    def on_epoch_end(self):
        """Shuffles order of ids at the end of each epoch if specified.
        """
        if self.shuffle:
            shuffle(self.ids)
            
    def _load(self, id):
        """Loads an image and its corresponding mask.

        Args:
            id (str): Filename of image (without extension).
        """
        # RGB or Grayscale for image
        if self.img_shape[2] == 1:
            color_mode = 'grayscale'
        elif self.img_shape[2] == 3:
            color_mode = 'rgb'

        # Load image as np.array
        img_path = self.imgs_dir/f'{id}.{self.imgs_ext}'

        img = load_img(
            img_path,
            color_mode=color_mode,
            target_size=self.img_shape[:2],
            interpolation='nearest'
        )
        img = img_to_array(img, dtype=np.uint8)

        # Load mask as np.array
        mask_path = self.masks_dir/f'{id}{self.masks_suffix}.{self.masks_ext}'

        mask = load_img(
            mask_path,
            color_mode='grayscale',
            target_size=self.img_shape[:2],
            interpolation='nearest'
        )
        mask = img_to_array(mask, dtype=np.uint8)

        # Perform any preprocessing
        if self.preproc:
            img, mask = self.preproc(img, mask)

        return img, mask

    def __getitem__(self, index):
        """
        Args:
            index (int): Meant to run from [0, len - 1]
        """
        # If running out of samples
        if (index + 1) * self.batch_size > len(self.ids):
            batch = self.ids[index * self.batch_size:]
        else:
            batch = self.ids[index * self.batch_size:(index + 1) * self.batch_size]

        # Create empty np.array instead?
        imgs = []
        masks = []

        for id in batch:
            _img, _mask = self._load(id)
            imgs.append(_img)
            masks.append(_mask)

        imgs = np.array(imgs)
        masks = np.array(masks)
        
        # Perform batch preprocessing
        # imgs = self._preprocess_imgs(imgs)
        # masks = self._preprocess_masks(masks)

        return imgs, masks

    def __len__(self):
        return int(np.ceil(len(self.ids) / self.batch_size))

    def name(self,index):
        return self.ids[index]

    def single_img_mask(self,index):
        return self._load(self.ids[index])
