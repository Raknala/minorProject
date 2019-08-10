import os
from django.shortcuts import render

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
import skimage
import numpy as np 
matplotlib.style.use('ggplot')
np.random.seed(1)
#from .vari import calcVegIndex
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request , 'index.html')

def upload(request):
    if request.method == 'POST' and request.FILES['img']:
        myfile = request.FILES['img']
        extension = myfile.name.split('.')[1]
        photo_path = 'static/img/' 
        if os.path.exists(photo_path + 'test.png'):
            os.remove(photo_path+'test.png')
        elif os.path.exists(photo_path + 'test.jpg'):
            os.remove(photo_path+'test.jpg')
        elif os.path.exists(photo_path + 'test.jpeg'):
            os.remove(photo_path+'test.jpeg')
        fs = FileSystemStorage()
        fs.save(photo_path+'test.'+ extension, myfile)
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
    #main code
    algorithm=request.POST['algorithm']
    if algorithm=='vari':
        red = image[:, :, 0].astype('float')
        blue = image[:, :, 2].astype('float')
        green = image[:, :, 1].astype('float')
        VARI = (green - red) / (red + green - blue + 10000)
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [ 'red','orange', 'yellow', 'green'])
        fig, ax = plt.subplots()
        ax.imshow(VARI,cmap=cmap)
        plt.axis('off')
        fig.savefig(photo_path+'result.'+extension, bbox_inches='tight')
        inputimg='img/test.'+extension
        outputimg='img/result.'+extension
        return render(request , 'output.html',{'outputimg':outputimg,'inputimg':inputimg})
    else:
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
        total = len(NDVI[0])*len(NDVI)
        print("total ndvi", total)

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
        extension = 'png'
        try:
            image=mpimg.imread('static/img/result.png')
        except:
            try:
                image=mpimg.imread('static/img/result.jpg')
                extension = 'jpg'
            except:
                image=mpimg.imread('static/img/result.jpeg')
                extension = 'jpeg'

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
                N_List.append(sublist)
        #print(lightness)
        # print(len(N_List))
        #print(len(L_List))
        #print(len(NDVI))

        x=N_List
        y=L_List
        np.corrcoef(x,y)
        plt.scatter(x,y)
        plt.show()
        #plt.savefig(photo_path+'plot.png', bbox_inches='tight')
        plt.close(fig)
    
        inputimg='img/test.'+extension
        outputimg='img/result.'+extension
        plotimg='img/plot.'+extension
        return render(request , 'output.html',{'outputimg':outputimg,'inputimg':inputimg,'dense':dense,'sparse':sparse,'barren':barren,'plotimg':plotimg})