import numpy as np
import pandas as pd
import os
import cv2
from IPython.display import Image


def textToBinary(text):
    if type(text)==str:
        result = ''.join([format(ord(i), "08b") for i in text])
        
    elif type(text) == int or type(text) == np.uint8:
        result = format(text, "08b")
        
    elif type(text) == bytes or type(text) == np.ndarray:
        result= [ format(i, "08b") for i in text ]
    
    else:
        raise TypeError("Verilen girdi karakter tipinde olmalıdır!")
        
    return result

def binaryToInteger(binary):
    temp = binary
    decimal, i =0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)

list1 = []

def encodeData(image):
    data = input("Encode edilecek metni girin (bos olmamali):")
    if(len(data)==0):
        raise ValueError('Metin bos')
        
    noBytes = (image.shape[0] * image.shape[1] * 3) // 8
    
    print("Encode edilebilecek maksimum byte:", noBytes)
    
    if(len(data)>noBytes):
        raise ValueError("Maksimum Byte sınırını astiniz, daha kucuk  bir metin deneyin!")

    data += '*****'
    
    dataBinary = textToBinary(data)
    dataLen = len(dataBinary)
    dataIndex = 0
    
    for i in image:
        for pixel in i:
            r, g, b = textToBinary(pixel)
            if dataIndex < dataLen:
                pixel[0] = int(r[:-1] + dataBinary[dataIndex], 2)
                dataIndex += 1
                list1.append(pixel[0])
                
            if dataIndex < dataLen:
                 pixel[1] = int(g[:-1] + dataBinary[dataIndex], 2) #changing to binary after overwrriting the LSB bit of Green Pixel
                 dataIndex += 1
                 list1.append(pixel[1])

            if dataIndex < dataLen:
                pixel[2] = int(b[:-1] + dataBinary[dataIndex], 2) #changing to binary after overwrriting the LSB bit of Blue pixel
                dataIndex += 1
                list1.append(pixel[2])

            if dataIndex >= dataLen:
                break
            
    cv2.imwrite('newImage.png',image)
    print("Mesaj gorselin (","newImage.png",") icine basariyla yerlestirildi")
                
image = cv2.imread("logo_iuc.png")

encodeData(image)


