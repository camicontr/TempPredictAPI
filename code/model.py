#Numpy
import numpy as np

#Tensorflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential, layers, callbacks
from tensorflow.keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional


# Create GRU model
def create_gru(units: int, X_train: np.array):
    model = Sequential()
    # Input layer 
    model.add(GRU(units=units, return_sequences=True, 
                 input_shape = [X_train.shape[1], X_train.shape[2]]))
    model.add(Dropout(0.3))
    # Hidden layer
    model.add(GRU(units=units))                
    model.add(Dropout(0.3))
    model.add(Dense(units=1))
    #Compile model
    model.compile(
        optimizer='adam',
        loss='mse'
        )
   
    return model


def fit_model(model: tf.keras.Model, X_train: np.array, y_train: np.array):
    early_stop = keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=2
        )

    history = model.fit(
        X_train,
        y_train,
        epochs=15,
        validation_split=0.2,
        batch_size=16,
        shuffle=False,
        callbacks=[early_stop]
        )
    return history
