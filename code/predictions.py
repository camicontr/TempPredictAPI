from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import numpy as np


# Loss
def plot_loss(history):
    plt.figure(figsize = (10, 6))
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Train vs Validation Loss')
    plt.ylabel('Loss')
    plt.xlabel('epoch')
    plt.legend(['Train loss', 'Validation loss'], loc='upper right')
    plt.show()


# Plot test data vs prediction
def plot_future(prediction, y_test):
    plt.figure(figsize=(10, 6))
    range_future = len(prediction)

    plt.plot(np.arange(range_future), np.array(y_test), label='Test data')
    plt.plot(np.arange(range_future), np.array(prediction),label='Prediction')

    plt.title("Test data vs prediction")
    plt.legend(loc='upper left')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Temperature Air (C)')
    plt.show()


# Make prediction
def prediction(model, X_test, scaler):
    prediction = model.predict(X_test)
    prediction = scaler.inverse_transform(prediction)
    return prediction


# Calculate RMSE
def evaluate_prediction(predictions, actual):
    rmse = np.sqrt(np.mean((predictions - actual)**2))
    print('Root Mean Square Error: {:.4f}'.format(rmse))
