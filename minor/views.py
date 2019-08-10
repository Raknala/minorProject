import os
from django.shortcuts import render
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

        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        import matplotlib.colors
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
        '''
        total=dense+sparse+barren
        dense=(dense/total)*100
        sparse=(sparse/total)*100
        barren=(barren/total)*100
        '''
        inputimg='img/test.'+extension
        outputimg='img/result.'+extension
        return render(request , 'output.html',{'outputimg':outputimg,'inputimg':inputimg,'dense':dense,'sparse':sparse,'barren':barren})