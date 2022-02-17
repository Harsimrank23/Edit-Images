from PIL import Image

img1=Image.open('dogs-subcategory-card.jpg') 
img1.save('dog1.png')
img1.show() 


img1=Image.open('dogs-subcategory-card.jpg')
MAX_SIZE=(250,250)
img1.thumbnail(MAX_SIZE) 
img1.save('dog_resize.jpg')
img1.show()

import os
for item in os.listdir():
    if item.endswith('.jpg'):
        img1=Image.open(item) 
        filename,extension=os.path.splitext(item)
        img1.save(f"{filename}.png") 


from PIL import ImageEnhance
img1=Image.open('dogs-subcategory-card.jpg')
#imageEnhancer is a module and sharpness is a class
enhancer=ImageEnhance.Sharpness(img1) #created object
enhancer.enhance(3).save('dog_wdit_0.jpg')
#0-blurry image
#1-original image
#2-image with increased sharpness
#3,4....-sharpness keep on increasing


#brightness
from PIL import ImageEnhance
img1=Image.open('dogs-subcategory-card.jpg')
#imageEnhancer is a module and Brightness is a class
enhancer=ImageEnhance.Brightness(img1) #created object
enhancer.enhance(1.12).save('dog_wdit_0.jpg')
#0-black image
#1-original image
#2-image with increased brightness
#3,4....-brightness keep on increasing


#color
from PIL import ImageEnhance
img1=Image.open('dogs-subcategory-card.jpg')
#imageEnhancer is a module and Color is a class
enhancer=ImageEnhance.Color(img1) #created object
enhancer.enhance(2).save('dog_wdit_0.jpg')
#0-black and white image
#1-original image
#2-image with increased color
#3,4....-colors keep on increasing


#contrast
from PIL import ImageEnhance
img1=Image.open('dogs-subcategory-card.jpg')
#imageEnhancer is a module and Contrast is a class
enhancer=ImageEnhance.Contrast(img1) #created object
enhancer.enhance(2).save('dog_wdit_0.jpg')
#0-grey image
#1-original image
#2-image with increased contrast
#3,4....-contrast keep on increasing


#image blur,GaussianBlur
#to blur image we can import filter ImageFilter
from PIL import ImageEnhance,ImageFilter
img1=Image.open('dogs-subcategory-card.jpg')
#to blur image we use GaussianBlur method
#img1.filter(ImageFilter.GaussianBlur())#here by default radius=2,we can adjust radius according to our choice
img1.filter(ImageFilter.GaussianBlur(radius=4   ))
img1.save('dog_wdit_0.jpg')
