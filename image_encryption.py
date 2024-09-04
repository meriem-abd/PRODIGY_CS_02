#encrypting/decrypting images
from PIL import Image
import numpy as np

def encrypt(path,value,save_path):
    try:
        image = Image.open(path)
    except IOError: #handling the case of a wrong path
        print(f"Error: Unable to open image at path {path}. Please check the path and try again.")
        return None
    image_array=np.array(image) #converting to an array
    pixel=image_array.copy() #copying image_array to pixel
    if len(image_array.shape) == 3:  # RGB image
        height, width, _ = image_array.shape #getting the dimensions
        channel=3
    else:  # Grayscale image
        height, width = image_array.shape
        channel=1
    for x in range(width):
        for y in range(height):
            #mathematical operations:
            new_x=int((x+value)%width)
            new_y=int((y-value)%height)
            # xor operations:
            new_y = new_y ^ value
            new_y = new_y % height
            new_x = new_x ^ value
            new_x = new_x % width
            #swaping pixels:
            if channel==3:
                pixel[y, x,:] = image_array[new_y, new_x,:]
            else:
                pixel[y, x] = image_array[new_y, new_x]
    #saving the encrypted image:
    new_image=Image.fromarray(pixel.astype('uint8')) #converting the array to an image
    new_image.save(save_path)
    return new_image

def decrypt(path,value,save_path):
    try:
        image = Image.open(path)
    except IOError:
        print(f"Error: Unable to open image at path {path}. Please check the path and try again.")
        return None
    image_array=np.array(image)
    pixel=image_array.copy()
    if len(image_array.shape) == 3:  # RGB image
        height, width, _ = image_array.shape
        channel=3
    else:  # Grayscale image
        height, width = image_array.shape
        channel=1
    for x in range(width):
        for y in range(height):
            # xor operations:
            new_y = y ^ value
            new_y = new_y % height
            new_x = x ^ value
            new_x = new_x % width
            #mathematical operations:
            new_x=int(((new_x-value)%width+width)%width)
            new_y=int(((new_y+value)%height+height)%height)
            #swaping pixels:
            if channel==3: #RGB
              pixel[y,x,:]=image_array[new_y,new_x,:]
            else:#GrayScale
                pixel[y,x]=image_array[new_y,new_x]
   #saving the decrypted image:
    new_image=Image.fromarray(pixel.astype('uint8'))
    new_image.save(save_path)
    return new_image
#taking the user's input:
path=input("enter the image's path:")
key=int(input("enter the encryption/decryption key: "))
save_path=input("enter the path to save the final image: ")
choice=int(input("do you want to encrypt (enter 1) or decrypt (enter 2)"))
while choice!=1 and choice!=2: #handling the user's input
    choice=input("enter 1 or 2: ")
if choice==1:
    new_image = encrypt(path,key,save_path)
    if new_image is not None:
        new_image.show() #opening the encrypted image
elif choice==2:
    new_image = decrypt(path,key,save_path)
    if new_image is not None:
        new_image.show() #opening the decrypted image
