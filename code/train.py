#Numpy
import numpy as np

#Pandas
import pandas as pd

#Tensorflow
import tensorflow as tf

#Auxiliar
from predictions import plot_loss, plot_future, prediction, evaluate_prediction
from model import create_gru, fit_model
from Prepro import Prepro
from pickle import dump


# Read data
dat = pd.read_csv("./data/temp_imputed.csv",
                sep=";",
                index_col=0
                )

# Train and test data split 
prepro = Prepro(dat)
feat = prepro.create_series("temp", "Date")

X_train, y_train, X_test, y_test, scaler = prepro.split_train_test(
    features=feat,
    split_size=0.9,
    look_back=30
)

# save the scaler
dump(scaler, open('./model/scaler.pkl', 'wb'))                                                       

# clear sesion tf
tf.keras.backend.clear_session()

# Create model, fit and save model
model_gru = create_gru(
    units=64, 
    X_train=X_train
    )
history_gru = fit_model(model_gru,
    X_train,
    y_train
    )
model_gru.save('./model/model_gru.h5')

# Model performance
plot_loss(history_gru)

# predictions
# Transform data back to original data space
y_test = scaler.inverse_transform(y_test)
y_train = scaler.inverse_transform(y_train)

prediction_gru = prediction(model_gru, X_test, scaler)

# Plot test data vs prediction
plot_future(prediction_gru, y_test)

# RMSE
evaluate_prediction(prediction_gru, y_test)
