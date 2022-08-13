#Python
import datetime

#Pickle
from pickle import load

#Numpy
import numpy as np

#Tensorflow
import tensorflow as tf


def predict_future(temp_prev: list, timesteps_to_predict: int=1):

    actual = scaler.transform(np.array(temp_prev).reshape(-1, 1)).flatten()
    for i in range(timesteps_to_predict):
        actual = np.append(actual, model.predict(actual[np.newaxis, :, np.newaxis]))[1:]

    return scaler.inverse_transform(actual.reshape(-1,1))


def get_model_response(input: dict):
    input_dict = input.dict() # from json object
    temp_prev = input_dict.get('temp_back')
    date = input_dict.get('date_init')

    prediction = predict_future(temp_prev)
    response = dict(zip([date + datetime.timedelta(hours=1)], prediction.ravel()[-1:])) 

    return response


scaler = load(open('./model/scaler.pkl', 'rb'))
model = tf.keras.models.load_model('./model/model_gru.h5')