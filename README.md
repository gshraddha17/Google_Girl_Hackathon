# ClimaMind : Unlocking Environmental Intelligence

<p align="center">
  <img alt="logo" src=ClimaMind_Logo.jpeg>
</p>


Discover the power of ClimaMind: Your Key to Environmental Intelligence. This dynamic website presents an interactive map showcasing crucial environmental data at your fingertips. Explore visualizations of air quality, water pollution, deforestation rates, and climate patterns. With ClimaMind, identify any flower and determine plant health with ease. By simply clicking a photo or viewing on the map, unveil valuable insights about soil types and the ideal plants for each. Stay informed about weather conditions in different locations. ClimaMind empowers you to make informed decisions and take action for a sustainable future.

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Map](#map)
- [Air Quality](#air-quality)
- [Water Pollution](#water-pollution)
- [Deforestation Patterns](#deforestation-patterns)
- [Climate Patterns](#climate-patterns)
- [Weather Type](#weather-type)
- [Waste Management](#waste-management)
- [Plant Health](#plant-health)
- [Soil Type](#soil-type)
- [Types of Flowers](#types-of-flowers)

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

### Process:

1. Data preparation and preprocessing: Read the dataset from city_hour.csv into a pandas DataFrame (df).
2. Split the dataset into features (X) and target (y) variables. Split the data into training and testing sets using train_test_split.
3. Perform feature scaling using StandardScaler to standardize the feature variables.
4. Build a Multi-Layer Perceptron (MLP) model using Sequential from tensorflow.keras. Define the model architecture with input and hidden layers.
5. Train the model using the training dataset.
6. Evaluate the trained model on the testing set to calculate the loss.
7. Save the trained model as model.h5 for future use.
8. Initialize the Flask application and load the saved model.
9. Implement a route in the Flask app to handle incoming POST requests for prediction.
10. Preprocess the input data, make predictions using the trained model, and return the results
11. Extract the required data from the query parameters.
12. Render the result.html template and pass the data for display.


### Flowchart:

<p align="center">
  <img alt="img" src=screenshots/Flowchart_Air.jpg>
</p>


### View:

This is the first page that opens if I click on Air Quality. I can click on any position of the map and will get the current Air Quality of that place.
<p align="center">
  <img alt="img" src=screenshots/Air_Model_1.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/Air_Model_2.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/Air_Model_3.jpg>
</p>


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

<p align="center">
  <img alt="img" src=screenshots/Flowchart_Deforestation.jpg>
</p>


### View:

<p align="center">
  <img alt="img" src=screenshots/Deforestation_1.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/Deforestation_2.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/Deforestation_3.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/Deforestation_4.jpg>
</p>

<p align="center">
  <img alt="img" src=screenshots/Deforestation_5.jpg>
</p>



## Climate Patterns


## Weather Type


## Waste Management

### Vision:

By developing an AI system for Waste Classification and ways of disposal, my work contributes to understanding the current state of the environment. Through real-time insights and visualizations, it enables informed decision-making, connecting waste management with critical environmental factors. Together, we can create a sustainable future and protect our environment.

### Process:

1. The code builds a waste classification model using a `Convolutional Neural Network (CNN) architecture` using `Waste-Classification-Data` dataset.
2. The dataset is loaded and preprocessed, converting the images to `RGB format` and storing the images and corresponding labels in separate lists.
3. `Data exploration` is performed to understand the distribution of waste classes in the dataset using pie charts and sample image visualizations.
4. The CNN model is constructed using the `Sequential API from Keras`. It consists of multiple `Conv2D and MaxPooling2D layers for feature extraction`, followed by Dense layers for classification.
5. The model is compiled with the `binary cross-entropy loss function, Adam optimizer`, and accuracy as the evaluation metric.
6. Image data generators are used to perform `data augmentation` and rescale the pixel values for the training and testing data.
7. The model is trained using the fit_generator function with the train_generator, and the training progress is visualized with accuracy and loss plots.
8. The model is evaluated on the test_generator, and the accuracy and loss metrics are plotted.
9. The predict_func function is defined to make predictions on individual images, displaying the predicted class label.
10. The trained model is saved as "Waste_Classification_Model.h5".
11. `A Flask web application` is created to allow users to upload waste images for classification.
12. The uploaded image is processed, and the model makes predictions on the image class.
13. The predicted class is displayed to the user along with disposal methods specific to that waste type.
14. The web application runs on a local server and can be accessed through a browser.

### Flowchart:

<p align="center">
  <img alt="img" src=screenshots/Flowchart_Waste.jpg>
</p>


### View:

<p align="center">
  <img alt="img" src=screenshots/Waste_Model_1.jpg>
</p>

I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Image_1_check_waste.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Waste_Model_2.jpg>
</p>

Then I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Image_2_waste_check.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Waste_Model_3.jpg>
</p>

## Plant Health

### Vision:

I have created a webpage that leverages real-time image analysis to provide instant and accurate assessments of plant health. By harnessing the power of advanced AI algorithms, the application swiftly determines whether a plant is healthy or diseased, empowering users with timely information to make informed decisions. This innovative solution merges technology and environmental awareness, revolutionizing the way we monitor and care for plant life. Together, we are paving the way towards a greener and more sustainable future.

### Process:

1. The code builds a dataframe from image data by extracting images through Kaggle dataset `plant-leaves-for-image-classification` and corresponding labels from the specified directories.
2. `Data augmentation techniques` are applied using the `ImageDataGenerator` to increase the training data and enhance model performance.
3. The `MobileNetV2` model is used as the base model, with the convolutional layers frozen to prevent retraining.
4. Additional layers are added on top of the base model for classification, including a global average pooling layer and dense layers.
5. The model is compiled with the Adam optimizer and categorical cross-entropy loss function.
6. The training data is fed to the model using the train_generator, and the model is trained for the `specified number of epochs`.
7. The model is evaluated on the test data using the test_generator, and the test loss and accuracy are calculated.
8. `A Flask web application` is created to allow users to upload images for waste classification.
9. The uploaded image is processed, preprocessed, and fed into the trained model for prediction.
10. The health of plant is displayed to the user. 
11. The application runs on a local server and can be accessed through a web browser.

### Flowchart:

<p align="center">
  <img alt="img" src=screenshots/Flowchart_Plant.jpg>
</p>

### View:

<p align="center">
  <img alt="img" src=screenshots/Plant_Model_1.jpg>
</p>

I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Image_1_check_health.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Plant_Model_2.jpg>
</p>

Then I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Image_2_check_health.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Plant_Model_3.jpg>
</p>


## Soil Type

### Vision:

* I have developed a soil classification model using a Convolutional Neural Network (CNN) architecture. To enhance the user experience, I integrated the MapBox API with my JavaScript code. This integration allows users to interact with a map displayed using the Leaflet library. By clicking anywhere on the map, an API call is triggered, capturing a satellite image of the selected location. This satellite imaging feature provides users with an alternative method to assess the soil without the need to upload an image. It offers real-time insights and visualizations of the current state of the environment either through map or uploading any image of your choice.

* To complement the soil classification results, the web application provides users with a list of suitable plants for the predicted soil type. This information empowers users to make informed decisions about plant selection based on the specific soil classification. With these features, my web application provides a user-friendly interface for soil classification and environmental analysis. It integrates advanced machine learning techniques with satellite imaging to offer a comprehensive understanding of soil patterns and environmental conditions.

### Process:

1. The soil classification model was developed using a `Convolutional Neural Network (CNN)` architecture.
2. The `Soil-Classification-Data dataset by Kaggle` was used for training the model.
3. The dataset was preprocessed by converting the images to RGB format and separating the images and corresponding labels.
4. `Data exploration techniques`, such as pie charts and sample image visualizations, were employed to analyze the distribution of soil classes in the dataset.
5. The CNN model was constructed using the `Sequential API from Keras`.
6. `Image data generators` were used for data augmentation and rescaling of pixel values during the training and testing phase.
7. The model was trained using the fit_generator function with the training data generator.
8. Training progress was monitored and visualized using accuracy and loss plots.
9. The trained soil classification model was saved as "Soil_Classification_Model.h5".
10. A Flask web application was created to provide a user-friendly interface for soil classification.
11. The web application offers two options to the users:
* Users can upload a soil image directly for classification. The uploaded image is processed, and the model predicts the soil class. The predicted class label is displayed to the user.
* Users can also view the soil through satellite imaging. The application integrates with satellite imagery services to display an aerial view of the soil. This provides users with an alternative method to assess the soil without needing to upload an image.


### Flowchart:

<p align="center">
  <img alt="img" src=screenshots/Flowchart_Soil.jpg>
</p>

### View:

<p align="center">
  <img alt="img" src=screenshots/Soil_Model_1.jpg>
</p>

I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Image_1_soil_check.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Soil_Model_2.jpg>
</p>

I used the second feature and clicked on the option `View on Map` and clicked at any place on the map.

<p align="center">
  <img alt="img" src=screenshots/Soil_Model_3.jpg>
</p>

This is the satellite image I got:

<p align="center">
  <img alt="img" src=screenshots/Soil_Model_4.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Soil_Model_5.jpg>
</p>



## Types of Flowers

### Vision:

My flower detection model complements the problem statement by leveraging real-time image analysis. By focusing on flower images, we contribute to a comprehensive understanding of the environment's biodiversity. This vision enables proactive environmental monitoring and management, fostering a sustainable and informed approach to environmental conservation.

### Process:

1. Used the Kaggle dataset `flowers-datset`; loaded the images and resized tehm to a common size.
2. Rescaled the pixel values.
3. Defined the `model architecture using convolutional layers, pooling layers, batch normalization, and activation functions`.
4. Added global average pooling and a fully connected layer for classification.
5. Save the best model based on validation accuracy using a model checkpoint callback.
6. Train the model using the training dataset for a `specified number of epochs`.
7. Defined a function to visualize the predicted probabilities for test images.
8. Selected random test images and display their predicted probabilities for each flower class.
9. Set up a `Flask web application` for deploying the flower classification model.
10. Load the trained model.
11. Handle image uploads, preprocess the uploaded image, make predictions using the model, and display the predicted class.

### Flowchart:

<p align="center">
  <img alt="img" src=screenshots/Flowchart_Flower.jpg>
</p>

### View:

<p align="center">
  <img alt="img" src=screenshots/Flower_Model_1.jpg>
</p>

I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Check_Flower_1.jpg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Flower_Model_2.jpg>
</p>

Then I uploaded the below image on the website.

<p align="center">
  <img alt="img" src=screenshots/Check_Flower_2.jpeg>
</p>

This is the result I got:

<p align="center">
  <img alt="img" src=screenshots/Flower_Model_3.jpg>
</p>
