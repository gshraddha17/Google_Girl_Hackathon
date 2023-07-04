from flask import Flask, render_template, request
import requests
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd
import numpy as np
import tensorflow as tf
import threading

app = Flask(__name__, template_folder="C:\\Users\\Mhsn\\Documents\\Google_Girl_Hackathon\\Weather_Analysis\\templates")
app.config['STATIC_URL_PATH'] = '/static'
def generate_and_save_plot(df, graph_path):
    plt.figure(figsize=(10, 6))
    plt.title('Weather Summary')
    sns.lineplot(data=df, dashes=False)
    plt.legend(df.columns)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Value')

    plt.savefig(graph_path)
    plt.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    country = request.form['country']
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    api_key = '6478d4b6a334141f6703dcc77737ac34'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()

    weather_info = []
    for data in weather_data['list']:
        weather_date = data['dt_txt'].split(' ')[0]
        if weather_date >= current_date:
            weather = {
                'date': weather_date,
                'precip_type': data['weather'][0]['main'],
                'temperature': data['main']['temp'],
                'apparent_temperature': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'wind_bearing': data['wind']['deg'],
                'visibility': data['visibility'],
                'loud_cover': data['clouds']['all'],
                'pressure': data['main']['pressure']
            }
            weather_info.append(weather)
            if len(weather_info) == 10:
                break

    df = pd.DataFrame(weather_info)
    df['Formatted Date'] = pd.to_datetime(df['date'])
    df.set_index('Formatted Date', inplace=True)
    df = df[['temperature', 'apparent_temperature', 'humidity', 'wind_speed', 'wind_bearing', 'visibility', 'loud_cover', 'pressure']]

    model = tf.keras.models.load_model('Weather_Analysis/Weather_Analysis.h5')

    # Generate and save the plot in a separate thread
    t = threading.Thread(target=generate_and_save_plot, args=(df, 'static/weather_graph.png'))
    t.start()

    return render_template('weather.html', graph_path='static/weather_graph.png')

if __name__ == '__main__':
    app.run(debug=True)
