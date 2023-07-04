from flask import Flask, jsonify, request, redirect, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model('Air/model.h5')
scaler = StandardScaler()

training_data = pd.read_csv('city_hour.csv')
numeric_columns = ['PM2.5', 'PM10', 'NO', 'NO2', 'NH3', 'CO', 'SO2', 'O3']
numeric_data = training_data[numeric_columns]

# Fit the scaler on numeric data
scaler.fit(numeric_data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    pm25 = data.get('PM2.5')
    pm10 = data.get('PM10')
    no = data.get('NO')
    no2 = data.get('NO2')
    nh3 = data.get('NH3')
    co = data.get('CO')
    so2 = data.get('SO2')
    o3 = data.get('O3')

    # Preprocess the input data
    input_data = pd.DataFrame([[pm25, pm10, no, no2, nh3, co, so2, o3]],
                              columns=['PM2.5', 'PM10', 'NO', 'NO2', 'NH3', 'CO', 'SO2', 'O3'])
    input_scaled = scaler.transform(input_data)

    # Make the prediction
    prediction = model.predict(input_scaled)[0].tolist()

    response = {
        'AQI': prediction
    }

    return jsonify(response)


@app.route('/result.html')
def result():
    aqi = request.args.get('aqi')
    co = request.args.get('co')
    no = request.args.get('no')
    no2 = request.args.get('no2')
    o3 = request.args.get('o3')
    so2 = request.args.get('so2')
    pm25 = request.args.get('pm25')
    pm10 = request.args.get('pm10')
    nh3 = request.args.get('nh3')

    return render_template('result.html', aqi=aqi, co=co, no=no, no2=no2, o3=o3, so2=so2, pm25=pm25, pm10=pm10, nh3=nh3)


if __name__ == '__main__':
    app.run()
