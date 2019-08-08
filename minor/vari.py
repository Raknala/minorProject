import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
def vari(img,extension,photo_path  ):
    extension = 'png'
    try:
        image=mpimg.imread('static/img/test.png')
    except:
        try:
            image=mpimg.imread('static/img/test.jpg')
            extension = 'jpg'
        except:
            image=mpimg.imread('static/img/test.jpeg')
            extension = 'jpeg'
    '''
    image=mpimg.imread('ok.jpg')
    red = image[:, :, 0].astype('float')
    blue = image[:, :, 2].astype('float')
    green = image[:, :, 1].astype('float')
    VARI = (green - red) / (red + green - blue + .001)
    '''

    NIR = image[:, :, 0].astype('float')
    blue = image[:, :, 2].astype('float')
    green = image[:, :, 1].astype('float')
    bottom = (blue - green) ** 2
    bottom[bottom == 0] = 1  # replace 0 from nd.array with 1
    VIS = (blue + green) ** 2 / bottom
    NDVI = (NIR - VIS) / (NIR + VIS)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','orange', 'yellow', 'green',])

    fig, ax = plt.subplots()


    #cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [  'yellow', 'green',])

    plt.imshow(NDVI,cmap=cmap)
    plt.axis('off')
    #extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #plt.savefig(photo_path+'result.'+extension, dpi=600,transparent=True, bbox_inches=extent, pad_inches=0)
    #plt.show()
    plt.savefig(photo_path+'result.'+extension, bbox_inches='tight')
    #plt.savefig(photo_path+'result.'+extension, bbox_inches=extent)
    #save_URL = 'static/img/result.' + extension
    #save here