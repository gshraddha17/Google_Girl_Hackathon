from flask import Flask, request, render_template, redirect, url_for
import os
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

app = Flask("Soil_Type", template_folder="Soil_Detection/templates")
model = keras.models.load_model('Soil_Detection/Soil_model.h5')
class_names = ['Alluvial soil', 'Clayey soils', 'Laterite soil', 'Loamy soil', 'Sandy loam', 'Sandy soil']
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'image' not in request.files:
            return render_template('index.html', message='No file uploaded')

        file = request.files['image']

        # Check if the file is empty
        if file.filename == '':
            return render_template('index.html', message='No file selected')

        # Check if the file is valid
        if file and allowed_file(file.filename):
            # Save the file to a temporary location
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            # Redirect to the result page with the image filename as a query parameter
            return redirect(url_for('result', image_filename=file.filename))

    # Render the index template by default
    return render_template('index.html')

@app.route('/satellite')
def satellite():
    return render_template('satellite.html')

@app.route('/result')
def result():
    # Retrieve the image filename from the query parameter
    image_filename = request.args.get('image_filename')

    # Generate the image URL or file path based on the filename
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

    # Load and preprocess the image
    image = load_and_preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(image)
    predicted_class_index = tf.argmax(predictions, axis=-1)[0]
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100

    # Render the result template with the predicted class and image path
    return render_template('result.html', predicted_class=predicted_class, image_path=image_path)

def load_and_preprocess_image(image_path):
    img = Image.open(image_path)
    gray_image = img.convert("L")
    resized_image = gray_image.resize((224, 224))
    image_array = np.array(resized_image)
    normalized_image = image_array / 255.0
    input_image = normalized_image.reshape((1, 224, 224, 1))
    return input_image

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):  # Create the uploads folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)
