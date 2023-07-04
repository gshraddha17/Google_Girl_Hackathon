from flask import Flask, render_template, request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

app = Flask(__name__, template_folder="C:\\Users\\Mhsn\\Documents\\Google_Girl_Hackathon\\Water\\templates")

# Load the pre-trained model and safe value ranges
model = joblib.load('Water/Water_Potability.joblib')
safe_value_ranges = {
    'ph': (6.5, 8.5),
    'Hardness': (0, 500),
    'Solids': (0, 500),
    'Chloramines': (0, 10),
    'Sulfate': (0, 500),
    'Conductivity': (0, 1000),
    'Organic_carbon': (0, 50),
    'Trihalomethanes': (0, 100),
    'Turbidity': (0, 10),
    # Add more parameters and their safe value ranges here
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get user input values
    data = pd.read_csv("Water/water_potability.csv")
    ph = float(request.form['ph'])
    hardness = float(request.form['Hardness'])
    solids = float(request.form['Solids'])
    chloramines = float(request.form['Chloramines'])
    sulfate = float(request.form['Sulfate'])
    conductivity = float(request.form['Conductivity'])
    organic_carbon = float(request.form['Organic_carbon'])
    trihalomethanes = float(request.form['Trihalomethanes'])
    turbidity = float(request.form['Turbidity'])
    # Create a DataFrame with user input values
    user_data = pd.DataFrame({
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfate],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
        # Add more parameters here based on your requirements
    })

    # Enable Matplotlib interactive mode
    plt.ion()

    # Create plots for each parameter
    plots = []
    for parameter in user_data.columns:
        # Create the plot for user-provided value
        plt.figure()
        plt.title(f'{parameter} - User Value')
        user_value = user_data[parameter].iloc[0]
        plt.axvline(x=user_value, color='red', label='User Value')
        plt.xlabel(parameter)
        plt.ylabel('Frequency')
        sns.histplot(data=data, x=parameter, color='blue', label='Safe Range')
        plt.legend()
        user_plot_path = f'static/user_plot_{parameter}.png'
        plt.savefig(user_plot_path)
        plt.close()

        # Create the plot for safe value range
        plt.figure()
        plt.title(f'{parameter} - Safe Value Range')
        plt.axvspan(safe_value_ranges[parameter][0], safe_value_ranges[parameter][1], alpha=0.3, color='green', label='Safe Range')
        plt.axvline(x=user_value, color='red', label='User Value')
        plt.xlabel(parameter)
        plt.ylabel('Frequency')
        sns.histplot(data=data, x=parameter, color='blue', label='Safe Range')
        plt.legend()
        safe_plot_path = f'static/safe_plot_{parameter}.png'
        plt.savefig(safe_plot_path)
        plt.close()

        # Append the paths of the generated plots
        plots.append((user_plot_path, safe_plot_path))

    return render_template('results.html', parameter=parameter, user_value=user_value, data=data, plots=plots)


if __name__ == '__main__':
    app.run(debug=True)
