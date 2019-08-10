import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
import skimage
matplotlib.style.use('ggplot')
np.random.seed(1)
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
    
        image   = mpimg.imread(photo_path+'result.'+extension)

        #NIR     = image.astype('float')

        NIR    = image[:, :, 0].astype('float')
        blue    = image[:, :, 2].astype('float')
        green   = image[:, :, 1].astype('float')

        # -----------------------------------------------------------------------------------------

        rgb_to_lab = skimage.color.rgb2lab(image, illuminant='D65', observer='2')

        lightness = rgb_to_lab[:, :, 0]

        bottom = (blue - green) ** 2
        bottom[bottom == 0] = .0001  # replace 0 from nd.array with 1
        VIS = (blue + green) ** 2 / bottom
        NDVI = (NIR - VIS) / (NIR + VIS)
        L_List = []
        for list in lightness:
            for sublist in list:
            L_List.append(sublist)

        N_List = []
        for list in NDVI:
            for sublist in list:
                N_List.append(sublist)\

        '''
        #print(lightness)
        print(len(N_List))
        print(len(L_List))
        #print(len(NDVI))
        '''
        x=N_List
        y=L_List
        np.corrcoef(x,y)
        plt.scatter(x,y)
        fig.savefig(photo_path+'plot.'+extension, bbox_inches='tight')

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