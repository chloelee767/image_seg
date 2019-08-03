import matplotlib.pyplot as plt

def plot_single(ax,dataframe,metrics):
    for m in metrics:
        ax.plot(dataframe['epoch'],dataframe[m],label=m)
    ax.legend(bbox_to_anchor=(1,1))

def plot_combined(dataframe):
    fig, ax = plt.subplots(nrows=3,figsize=(7,14))
    plot_single(ax[0],dataframe,['val_iou_score','test_iou_score','val_f_score','test_f_score'])
    plot_single(ax[1],dataframe,['loss','test_loss','val_loss'])
    plot_single(ax[2],dataframe,['lr'])
    plt.show()

def plot_and_save(dataframe,save_as):
    plot_combined(dataframe)
    plt.save_fig(str(save_as),bbox_inches='tight')
    plt.clf()
