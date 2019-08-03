import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img,img_to_array
from ..configs.default import IMGDIR,MASKDIR

def save_preds(preds,img_names,save_to):
    save_to = Path(save_to)
    save_to.mkdir(exist_ok=True,parents=True)
    num_preds = preds.shape[0]
    target_size = preds.shape[1:3]
    fig, ax = plt.subplots(ncols = 2,figsize=(10,10))
    for i in range(num_preds):
        img = load_img(str(IMGDIR/f'{img_names[i]}.jpg'),color_mode='rgb',target_size=target_size,interpolation='nearest')
        img = img_to_array(img,dtype=np.uint8)
        
        truth = load_img(str(MASKDIR/f'{img_names[i]}.png'),color_mode='grayscale',target_size=target_size,interpolation='nearest')
        truth = np.squeeze(img_to_array(truth,dtype=np.uint8))
        
        pred = np.squeeze((preds[i] * 255).astype('uint8'))
        
        ax[0].imshow(img)
        ax[0].imshow(pred,cmap='gray',alpha=0.4)
        ax[0].set_title(f'Prediction ({img_names[i]})')
        ax[1].imshow(img)
        ax[1].imshow(truth,cmap='gray',alpha=0.4)
        ax[1].set_title('Ground Truth')
        
        plt.savefig(save_to/f'{img_names[i]}.jpg',bbox_inches='tight')
        ax[0].clear()
        ax[1].clear()

