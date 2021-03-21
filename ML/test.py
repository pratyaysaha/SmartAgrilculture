from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Convolution2D,Dense,MaxPool2D,Activation,Dropout,Flatten
from keras.layers import GlobalAveragePooling2D
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.layers.normalization import BatchNormalization
import os 
import pandas as pd
import plotly.graph_objs as go
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
test = pd.read_csv('test.csv')
test['image_id'] = test['image_id'] +'.jpg'
train_datagen = ImageDataGenerator( horizontal_flip=True,
    vertical_flip=True,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=.1,
    fill_mode='nearest',
    shear_range=0.1,
    rescale=1/255,
    brightness_range=[0.5, 1.5])
model = load_model('my_model.hdf5')
test_generator=train_datagen.flow_from_dataframe(test,directory='/home/subhidh/Desktop/P/test',
                                                      target_size=(128,128),
                                                      x_col="image_id",
                                                      y_col=None,
                                                      class_mode=None,
                                                      shuffle=False,
                                                      batch_size=16)
probs_RESNET = model.predict(test_generator, verbose=1)
#print(probs_RESNET[0][0])
if(probs_RESNET[0][0]>.95):
    print("healthy")
if(probs_RESNET[0][1]>.95):
    print("multiple disease")
if(probs_RESNET[0][2]>.95):
    print("rust")
if(probs_RESNET[0][3]>.95):
    print("scab")
