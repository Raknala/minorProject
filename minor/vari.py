import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
def calcVegIndex(img,extension,photo_path,num=0):
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
    if num==1:#calculating ndvi
        NIR = image[:, :, 0].astype('float')
        blue = image[:, :, 2].astype('float')
        green = image[:, :, 1].astype('float')
        bottom = (blue - green) ** 2
        bottom[bottom == 0] = 1  # replace 0 from nd.array with 1
        VIS = (blue + green) ** 2 / bottom
        NDVI = (NIR - VIS) / (NIR + VIS)
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','orange', 'yellow', 'green'])
        fig, ax = plt.subplots()
        ax.imshow(NDVI,cmap=cmap)
        plt.axis('off')
        fig.savefig(photo_path+'result.'+extension, bbox_inches='tight')

    else:#calculating vari
        red = image[:, :, 0].astype('float')
        blue = image[:, :, 2].astype('float')
        green = image[:, :, 1].astype('float')
        VARI = (green - red) / (red + green - blue + 10000)
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','orange', 'yellow', 'green'])
        fig, ax = plt.subplots()
        ax.imshow(VARI,cmap=cmap)
        plt.axis('off')
        fig.savefig(photo_path+'result.'+extension, bbox_inches='tight')