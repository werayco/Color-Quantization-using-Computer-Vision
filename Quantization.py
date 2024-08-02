import matplotlib.image as img
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
import cv2 as cv
import os
import time
from datetime import datetime
from functools import cache,lru_cache


class imgQuantization:
    '''This is used for image quantization, more like thresholding your image into two or more distinct colors using the kmeans clustering algorithm '''
    def __init__(self,img_path:str,clusters:int,algorun):
        self.img_path = img_path
        self.clusters = clusters
        self.algorun = algorun

    def __str__(self):
        '''this method serves as a string representation of your class'''
        return f" the name of the image used is {os.path.dirname(self.img_path)}"
    
    @cache
    def imgread(self):
        '''this method basically opens the img, we can use the Python Imaging Library(PIL) or just Matplotlib, uncomment the one you wish'''
        img_using_PIL = Image.open(self.img_path)
        img_using_matpltlib = img.imread(self.img_path)

        height,width,channel = cv.imread(self.img_path).shape
        return (img_using_matpltlib,channel)
    
    @cache
    def Quantization(self):
        img, channel = self.imgread()
        img_reshaped = img.reshape(-1, channel)  # Normalize the image data

        # Initializing our KMeans classifier
        kmeans_seg = KMeans(n_clusters=self.clusters, n_init=self.algorun)
        kmeans_seg.fit(img_reshaped)

        # Mapping the cluster centers (2D) to the labels (1D)
        seg_img = kmeans_seg.cluster_centers_[kmeans_seg.labels_] # the cluster_centers are just the array representations of the clusters, which are in 2d
        print(seg_img)
        seg_img = seg_img.reshape(img.shape)
        # plt.savefig(seg_img,"img.png")

        plt.imshow(seg_img)
        plt.axis('off')
        plt.show()
        # plt.savefig("quantized_image.png") # uncomment if you need to save the output as a png file

img_seg_obj = imgQuantization("C:\\Users\\LENOVO-PC\\Pictures\\TDATT.png",3,10)
img_seg_obj.imgread()
img_seg_obj.Quantization()
