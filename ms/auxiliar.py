#Python
import datetime

#Pickle
from pickle import load

#Numpy
import numpy as np

#Tensorflow
import tensorflow as tf


def predict_future(temp_prev: list, timesteps_to_predict: int):

    actual = scaler.transform(np.array(temp_prev).reshape(-1, 1)).flatten()
    for i in range(timesteps_to_predict):
        actual = np.append(actual, model.predict(actual[np.newaxis, :, np.newaxis]))[1:]

    return scaler.inverse_transform(actual.reshape(-1,1))


def get_model_response(input: dict):
    input_dict = input.dict() # from json object

    temp_prev = input_dict.get('temp_back')
    timesteps = input_dict.get('time_steps')
    date =  input_dict.get('date_init')

    prediction = predict_future(temp_prev, timesteps)
    response = dict(zip([date + datetime.timedelta(hours = t+1) for t in range(timesteps)], 
     prediction.ravel()[-timesteps:])) 

    return response


scaler = load(open('./model/scaler.pkl', 'rb'))
model = tf.keras.models.load_model('./model/model_gru.h5')