import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
from PIL import Image, ImageEnhance
import skimage
import cv2
import numpy as np 
matplotlib.style.use('ggplot')
np.random.seed(1)

def calcVegIndex(img,nir,extension,photo_path,num=0):
    #extension = 'png'
    '''
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
    if num==1:
        image=mpimg.imread(img)
        #normalizedImg = np.zeros((800, 800))
        #image = cv2.normalize(image, normalizedImg, 0, 255, cv2.NORM_MINMAX)  
        #image = cv2.normalize(image, normalizedImg, 0, 255, cv2.NORM_MINMAX) 
        #image = cv2.fastNlMeansDenoisingColored(image, None, 3, 3, 7, 21)
         
        green = image[:, :, 0].astype('float')
        blue = image[:, :, 2].astype('float')
        new = image[:, :, 1].astype('float')
        bottom = (blue - new) ** 2
        bottom[bottom == 0] = 1  # replace 0 from nd.array with 1
        red = (blue + new) ** 2 / bottom
        bot=green + red
        bot[bot==0]=0.0001
        VARI = (green - red) / (bot) 
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','yellow','green'])
        fig, ax = plt.subplots()
        ax.imshow(VARI,cmap=cmap)
        plt.axis('off') 
        fig.savefig(photo_path+'result.'+extension, bbox_inches='tight')
        plt.clf()
        '''
        rgb_to_lab = skimage.color.rgb2lab(image, illuminant='D65', observer='2')

        lightness = rgb_to_lab[:, :, 0]

        L_List = []
        for list in lightness:
            for sublist in list:
                L_List.append(sublist)

        N_List = []
        for list in NDVI:
            for sublist in list:
                N_List.append(sublist)
        x=N_List
        y=L_List
        np.corrcoef(x,y)
        plt.scatter(x,y)
        fig.savefig(photo_path+'plot.png', bbox_inches='tight')
        '''
        dense = 0
        sparse = 0
        barren = 0
        for list in VARI:
            for sublist in list:
                if (sublist>= 0.6):
                    dense += 1
                elif (sublist<0.6 and sublist>=0.2):
                    sparse += 1
                elif (sublist< 0.2):
                    barren += 1
        total=dense+sparse+barren
        dense=round((dense/total)*100,3)
        sparse=round((sparse/total)*100,3)
        barren=round((barren/total)*100,3)
        return dense,sparse,barren
    else:
            image = plt.imread(img)
            normalizedImg = np.zeros((800, 800))
            normalizedImg = cv2.normalize(image, normalizedImg, 0, 255, cv2.NORM_MINMAX)  
            #image = cv2.fastNlMeansDenoisingColored(image, None, 3, 3, 7, 21)
            image = cv2.normalize(image, normalizedImg, 0, 255, cv2.NORM_MINMAX)  
            image_nir=mpimg.imread(nir)
            NIR = image_nir
            red=image[:,:,0].astype('float')
            NDVI=(NIR-red)/(NIR+red)
            cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','yellow', 'green'])
            fig, ax = plt.subplots()
            ax.imshow(NDVI,cmap=cmap)
            plt.axis('off') 
            fig.savefig(photo_path+'result.'+extension, bbox_inches='tight')
            plt.clf()
            '''
            rgb_to_lab = skimage.color.rgb2lab(image, illuminant='D65', observer='2')

            lightness = rgb_to_lab[:, :, 0]

            L_List = []
            for list in lightness:
                for sublist in list:
                    L_List.append(sublist)

            N_List = []
            for list in NDVI:
                for sublist in list:
                    N_List.append(sublist)
            x=N_List
            y=L_List
            np.corrcoef(x,y)
            plt.scatter(x,y)
            fig.savefig(photo_path+'plot.png', bbox_inches='tight')
            '''
            dense = 0
            sparse = 0
            barren = 0
            for list in NDVI:
                for sublist in list:
                    if (sublist>= 0.6):
                        dense += 1
                    elif (sublist<0.6 and sublist>=0.2):
                        sparse += 1
                    elif (sublist< 0.2):
                        barren += 1
            total=dense+sparse+barren
            dense=round((dense/total)*100,3)
            sparse=round((sparse/total)*100,3)
            barren=round((barren/total)*100,3)
            return dense,sparse,barren