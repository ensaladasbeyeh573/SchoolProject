import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Set CUDA device ID

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

input_data = [2.5, 3.7, 4.8, 1.9, 2.6, 3.4]  # Example input data

model = Sequential()
model.add(LSTM(32, input_shape=(input_data.shape[1], input_data.shape[2]), return_sequences=True))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')
