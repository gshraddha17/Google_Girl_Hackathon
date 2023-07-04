from flask import Flask, render_template, request
import pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import traceback

app = Flask('Deforestation', template_folder='Deforestation/templates')
app.config['STATIC_URL_PATH'] = '/static'

# Load the ARIMA model
with open('Deforestation/arima_model.pkl', 'rb') as f:
    arima_model = pickle.load(f)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for generating visualizations
@app.route('/result', methods=['POST'])
def visualizations():
    # Get the country name from the form data
    country = request.form['country']

    # Read the dataset
    df = pd.read_csv('Deforestation/annual-change-forest-area.csv')

    # Filter data for the selected country
    print(df['Entity'].unique())  # Print unique country names for debugging
    country_data = df[df['Entity'].str.lower() == country.lower()]

    if not country_data.empty:
        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Plot the actual deforestation rates
        plt.plot(country_data['Year'], country_data['Net forest conversion'], marker='o', label='Actual')

        # Forecast using the ARIMA model
        try:
            forecast_values = arima_model.forecast(steps=35)
            print(forecast_values)  # Print forecast values for debugging

            if len(forecast_values) == 0:
                raise ValueError("No forecast values generated.")

            # Get the last available year in the dataset
            last_year = country_data['Year'].max()

            # Create the forecast years
            forecast_years = range(last_year + 1, last_year + 36)

            # Plot the forecasted deforestation rates
            plt.plot(forecast_years, forecast_values, marker='o', label='Forecasted')

            # Set the axis labels and title
            plt.xlabel('Year')
            plt.ylabel('Net Forest Conversion')
            plt.title(f'Deforestation Rates for {country} (2023-2057)')

            # Add legend
            plt.legend()

            # Save the plot to a file
            plt.savefig('static/forecast.png')
              # Save the plot in the static folder

            return render_template('result.html', country=country)

        except Exception as e:
            traceback.print_exc()  # Print the traceback for debugging
            return render_template('error.html', error_message='Error occurred during forecast generation.')

if __name__ == '__main__':
    app.run(debug=True)
