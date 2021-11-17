from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import urllib.request
import os
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow import keras
import cv2 as cv
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        #print(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        #print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return redirect(url_for('predict', filename = filename))
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/predictions/<filename>')
def predict(filename):
    absolute_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename)
    image = cv.imread(absolute_path, cv.IMREAD_GRAYSCALE)
    print(image)
    image = cv.resize(image, (28,28))
    image = image/255
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=3)
    model = keras.models.load_model('CNN_model_1')
    preds = model.predict(image)
    preds = np.squeeze(preds)
    
    digit_predicted = str(np.argmax(preds))
    preds_probabilities = dict([(str(i), str(preds[i])) for i in range(10)])
    
    return jsonify(filename = filename, digit_predicted = digit_predicted, preds_probabilities = preds_probabilities)
    #return render_template("found.html",keys=email, obj=listOfObjects)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    print(request.files)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)