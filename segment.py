# -*- coding: utf-8 -*-
# ! python3
import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

# img=cv2.imread(r'C:\Users\16609\Desktop\output\P1100500\1.png')
# img0=cv2.imread(r'C:\Users\16609\Desktop\input\P1100502.JPG')
# cv2.imshow('aaa',img0)
# # cv2.waitKey(0)
# a=plt.imread(r'C:\Users\16609\Desktop\input\P1100502.JPG')
# b=plt.imread(r'C:\Users\16609\Desktop\output\P1100500\1.png')
name='P1100547'
for i in range(0,255):
    image1=Image.open(r'C:\Users\16609\Desktop\output'+'\\'+str(name)+'\\'+str(i)+'.png').convert('RGB')
    image2 = Image.open(r'C:\Users\16609\Desktop\input'+'\\'+str(name)+'.JPG').convert('RGB')
     # 获取图像的宽度和高度
    width, height = image1.size
     # 创建一个新的空白图像，用于存储结果
     # 遍历图像的每个像素，并根据 image1 进行掩盖
    for x in range(width):
         for y in range(height):
             # 获取当前位置的像素值
             pixel_value = image1.getpixel((x, y))
             if pixel_value == (0,0,0):
                 image2.putpixel((x, y), pixel_value)
             else:
                 pass
    image2.save(r'C:\Users\16609\Desktop\output'+'\\'+str(name)+'\\'+str(i)+'.png')

boxmes=pd.read_csv(r'C:\Users\16609\Desktop\output'+'\\'+str(name)+'\\'+'metadata.csv',delimiter=',',skiprows=0).values
for i in range(len(boxmes[:,0])):
    image1 = Image.open(r'C:\Users\16609\Desktop\output'+'\\'+str(name)+'\\'+str(i)+'.png').convert('RGB')
    c=image1.crop((boxmes[i,2],boxmes[i,3],boxmes[i,2]+boxmes[i,4],boxmes[i,3]+boxmes[i,5]))
    c.save(r'C:\Users\16609\Desktop\output'+'\\'+str(name)+'\\'+str(i)+'.png')



