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
