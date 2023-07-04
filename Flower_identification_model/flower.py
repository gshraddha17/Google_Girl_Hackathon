from flask import Flask, request, render_template
import os
import tensorflow as tf
from tensorflow import keras
from PIL import Image

app = Flask("Flower_Model", template_folder="Flower_identification_model\\templates")
model = keras.models.load_model('Flower_identification_model\\flower_model.h5')
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
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
            
            # Load and preprocess the image
            image = load_and_preprocess_image(image_path)
            
            # Make predictions
            predictions = model.predict(image)
            predicted_class_index = tf.argmax(predictions, axis=-1)[0]
            predicted_class = class_names[predicted_class_index]
            confidence = predictions[0][predicted_class_index] * 100
            
            # Render the result template with the predicted class
            return render_template('result.html', predicted_class=predicted_class, confidence=confidence)
        
    # Render the index template by default
    return render_template('index.html')

def load_and_preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = img / 255.0
    img = tf.expand_dims(img, axis=0)
    return img

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):  # Create the uploads folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()