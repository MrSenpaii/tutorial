# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#load data
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()


#look variable data types
print(type(x_train))
print(type(y_train))
print(type(x_test))
print(type(y_test))


#get the shape of arrays

print('x_train shape:',x_train.shape)
print('y_train shape:',y_train.shape)
print('x_test.shape:',x_test.shape)
print('y_test.shape:',y_test.shape)

#look firstimage

index = 0
x_train[index]

#show as picture

img = plt. imshow(x_train[index])

#image label

print('the image label is:', y_train[index])

# get image clasification

clasification = ['airplane','bird','cat','deer','dog','frog','horse','ship','truck']

print('the image class is;', clasification[y_train[index][0]]
      

 


