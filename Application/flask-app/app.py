from flask import Flask, redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename

from fastai import *
from fastai.vision import *
import numpy as np 
import urllib.request
import os

path = os.path.dirname(os.path.realpath(__file__))

def classify(image_path):
    model_name = 'PneumoniaRESNET50.pkl'
    model_path = path + str('\\models')
    learn = load_learner(model_path,model_name)
    category, tensor, probability = learn.predict(open_image(image_path))
    return category, probability
    

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():

    f = request.files['file']
    image_path = os.path.join(path, 'tmp', secure_filename(f.filename))
    f.save(image_path)

    category, probability = classify(image_path)
    print(category,probability)

    response = jsonify({
			"result": str(category),
            "percent": round(float(max(probability))*100,2)  
			})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run()   