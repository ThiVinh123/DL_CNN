#from memory_profiler import memory_usage
import os
import pandas as pd
from glob import glob
import numpy as np
from keras import layers
from keras import models
from tensorflow.keras.layers import LeakyReLU
from keras.optimizers import Adam
import keras.backend as K
import librosa
import librosa.display
import pylab
import matplotlib.pyplot as plt
from matplotlib import figure
import gc
from path import Path
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from keras.models import Sequential, Model
from keras.layers import Conv2D, MaxPooling2D
from keras import regularizers, optimizers
import pandas as pd
import numpy as np
from keras_preprocessing.image import ImageDataGenerator

train_data_path='data/train/'
test_data_path='data/test/'
wav_path = 'data/wav/'

# Ham tao ra spectrogram tu file wav
def create_spectrogram(filename,name, file_path):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72,0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename  = file_path + name + '.png'
    plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,S

# Lap trong thu muc data/wav/train va tao ra 4000 file anh spectrogram
Data_dir=np.array(glob(wav_path+"train.csv/*"))

for file in Data_dir[0:4000]:
    filename,name = file,file.split('/')[-1].split('.')[0]
    create_spectrogram(filename,name, train_data_path)

gc.collect()

# Lap trong thu muc data/wav/test va tao ra 3000 file anh spectrogram
Test_dir=np.array(glob(wav_path+"test.csv/*"))


for file in Test_dir[0:3000]:
    filename,name = file,file.split('/')[-1].split('.')[0]
    create_spectrogram(filename,name,test_data_path)

gc.collect()

print("Process done!")
