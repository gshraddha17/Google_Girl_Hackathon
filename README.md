# ClimaMind : Unlocking Environmental Intelligence

<p align="center">
  <img alt="logo" src=ClimaMind_Logo.jpeg>
</p>


Discover the power of ClimaMind: Your Key to Environmental Intelligence. This dynamic website presents an interactive map showcasing crucial environmental data at your fingertips. Explore visualizations of air quality, water pollution, deforestation rates, and climate patterns. With ClimaMind, identify any flower and determine plant health with ease. By simply clicking a photo or viewing on the map, unveil valuable insights about soil types and the ideal plants for each. Immerse yourself in captivating animations of diverse landscapes. Stay informed about weather conditions in different locations. Plus, gain valuable waste management guidance and access a comprehensive ranking of global countries. ClimaMind empowers you to make informed decisions and take action for a sustainable future.

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Map](#map)
- [Air Quality](#air-quality)
- [Water Pollution](#water-pollution)
- [Deforestation](#deforestation-rates)
- [Climate Patterns](#climate-patterns)
- [Weather Type](#weather-type)
- [Waste Management](#waste-management)
- [Rankings](#rankings)
- [Plant Health](#plant-health)
- [Soil Type](#soil-type)
- [Types of Flowers](#types-of-flowers)
- [Types of Landscape](#types-of-landscape)

## Installation

To use ClimaMind, please follow these steps:

1. Clone the repository or download the code files.

2. Install the required dependencies by running the following command:

```shell
pip install -r requirements.txt
```
3. Obtain API Keys:
   -> OpenWeatherMap API Key: Sign up on OpenWeatherMap and get an API key.
   -> MapBox API Key: Sign up on Mapbox and get an API key.

5. Set environment variables:
   * Create a .env file in the project directory.
   * Add the following environment variables and replace the values with your API keys and preferences:
   * Replace the placeholders with your own values.
   
```plaintext
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
MAPBOX_API_KEY=your_ampbox_api_key
```

5. You can use Microsoft Visual Studio Code to open the directory and terminal.

<p align="center">
  <img alt="VS Code in action" src="https://user-images.githubusercontent.com/35271042/118224532-3842c400-b438-11eb-923d-a5f66fa6785a.png">
</p>



### Set up your environment

-   **Step 1.** [Install a supported version of Python on your system](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) 
-   **Step 2.** [Install the Python extension for Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-gallery).

-   Select your Python interpreter by clicking on the status bar

     <img src=https://raw.githubusercontent.com/microsoft/vscode-python/main/images/InterpreterSelectionZoom.gif width=280 height=100>


6. You can use `Google Colaboratory` or `Jupyter Notebooks` to run the models(train and test them)
7. Sign Up on `Kaggle` to download the datasets. 


## Usage

1. View `index.html` of the `root directory` on browser.

<p align="center">
  <img alt="img" src=screenshots/main_page1.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/main_page2.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/main_page3.jpg>
</p>


2. For all folders which have `Flask` usage run the `.py` file. A development server will set up which will show you the link where you can view the `index.html` of that directory.

<p align="center">
  <img alt="img" src=screenshots/terminal_flask.jpg>
</p>


## Map



## Air Quality



## Water Pollution


## Deforestation Patterns

### Process:

1. The code uses `'annual-change-forest-area.csv' dataset`.
2. A preliminary `data exploration` is performed to gain initial insights into the dataset. 
3. `Data visualization techniques by Matplotlib`, are employed to create visually compelling and informative plots. Histograms, line plots, box plots, and bar plots are generated to reveal the distribution and temporal patterns of net forest conversion values across different countries. These visualizations aid in understanding deforestation trends and their geographical variations.
4. `Feature engineering techniques` are applied to extract additional valuable information from the dataset. Grouping the data by country allows for the calculation of essential metrics such as total deforestation, average deforestation rate, and the number of years covered by the dataset. These metrics are consolidated into a new dataframe, enabling further analysis and comparison.
5. The code utilizes TensorFlow to develop an `LSTM model for time series forecasting`. The LSTM model is trained using the provided training dataset, with the architecture comprising a single LSTM layer followed by a dense layer. The model is optimized using the `Adam optimizer` and trained to `minimize the mean squared error (MSE)`. The input data is reshaped to match the required format of the LSTM model.
6. The trained LSTM model is evaluated using the test dataset to assess its predictive performance. The mean squared error (MSE) is calculated to quantify the deviation between the predicted and actual values.
7. To further analyze the time series data, the code incorporates the `ARIMA model from the statsmodels library`. The ARIMA model is fitted to the training data, enabling the generation of forecasts for the test data. The mean squared error (MSE) is computed to evaluate the accuracy of the forecasted values.
8. The ARIMA model is serialized using the pickle library, allowing it to be saved in a file named `'arima_model.pkl'`. This enables convenient storage and retrieval of the model for future predictions without the need for retraining.
9. The code progresses to develop a dynamic and user-friendly `Flask web application`. The web application provides an interactive interface for users to generate visualizations and forecasts based on their inputs. The ARIMA model, previously saved using pickle, is loaded within the application to enable efficient forecasting. Matplotlib is utilized to create informative plots illustrating the actual and forecasted deforestation rates for the selected country. The resulting plot is saved in the static folder and presented to the user, providing a comprehensive understanding of deforestation patterns and trends.


### Flowchart:



### View:

<p align="center">
  <img alt="img" src=screenshots/deforestation_1.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/deforestation_2.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/deforestation_3.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/deforestation_4.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/deforestation_5.jpg>
</p>



## Climate Patterns


## Weather Type


## Waste Management


## Rankings



## Plant Health


## Soil Type



## Types of Flowers


## Types of Landscape
