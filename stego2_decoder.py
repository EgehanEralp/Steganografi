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

def decodeData(image):
    binaryData=""
    for i in image:
        for pixel in i:
            r, g, b= textToBinary(pixel)
            binaryData += r[-1]
            binaryData += g[-1]
            binaryData += b[-1]
            
    allBytes = [binaryData[i: i+8] for i in range(0, len(binaryData), 8)]
        
    decodedData=""
    for byte in allBytes:
        decodedData += chr(int(byte, 2))
        
        if decodedData[-5:] == "*****":
            break
    print("Gorsel icine gizlenmis metin:",decodedData[:-5])
    
image = cv2.imread("newImage.png")
decodeData(image)