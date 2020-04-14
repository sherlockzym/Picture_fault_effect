# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:30:27 2020

@author: logic
"""


#from PIL import Image, ImageDraw, ImageFont
from PIL import Image
import numpy as np



def add_effect(filepath, outpath):
    img_orig = Image.open(filepath)     #打开文件
    img_orig.putalpha(255) #

    array_orig = np.array(img_orig)     #将图片转化为三维数组
    array_r = np.copy(array_orig)   #复制原图的三维数组
    array_r[:,:,1:3] = 0    #将G和B通道的值设为0，只剩下R(red)通道的值非0
    image_r = Image.fromarray(array_r)  #array转化为image

    array_gb = np.copy(array_orig)  #生成GB通道的图片，只需要把R通道的值设为0
    array_gb[:,:,0] = 0
    image_gb = Image.fromarray(array_gb)

     #生成一张黑色背景的画布，把R通道的图片贴在画布上，这里粘贴的位置设成 (5, 5) 是为了与GB通道的图片错开位置
    canvas_r = Image.new("RGB", img_orig.size, color=(0,0,0))  
    canvas_r.paste(image_r, (5, 5), image_r)
    
    #对于GB通道的图片也是类似，贴在另一张画布上，粘贴的位置设成 (0, 0)，与上面R通道的图片错开一定位置
    canvas_gb = Image.new("RGB", img_orig.size, color=(0,0,0))
    canvas_gb.paste(image_gb, (0,0), image_gb)
    
    result_array = np.array(canvas_r) + np.array(canvas_gb)
    result = Image.fromarray(result_array)
    result.show()
    
    result = result.crop((5, 5, img_orig.size[0], img_orig.size[1]))     #crop函数--图片裁剪操作
    #axis = 0，返回该二维矩阵的行数  axis = 1，返回该二维矩阵的列数

    result.save(outpath)
    
out =('./output_cyberpunk.png')

add_effect('./cyberpunk.jpg', out)



