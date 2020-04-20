import numpy as np
import pandas as pd
import cv2
import argparse

#Global variables
clicked = False
r = g = b = xpos = ypos = 0

#Arguement Parser to input image link
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading image with OpenCV
img = cv2.imread(img_path)

#Reading CSV with Pandas
index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index. header=None)

#Function to calculate minimum distance from all colors

#Function to get xpos and ypos from click