from flask import Flask, render_template, request
import pickle
import logging
import os

# dir paths
base_dir = os.getcwd()
models_dir = os.path.join(base_dir, 'models', 'linear_model')
logs_dir = os.path.join(base_dir, 'logs')

# file paths
in_file = os.path.join(models_dir, 'linear_model.pkl') #model
log_file = os.path.join(logs_dir, 'app.log') #logs


# configure logs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', filename=log_file, filemode='a')

# current running file
logging.info("Running file %s", os.path.basename(__file__))

# Loading trained model
logging.info("Loading trained model from %s", in_file)
model = None
with open(in_file, 'rb') as f:
    model = pickle.load(f)


app = Flask(__name__)


# Route to landing page
@app.route('/', methods=['GET']) 
def index():
    logging.info("Route handler for landing page called")
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
    logging.info("Route handler for predicting price called")
    rooms = int(request.form['rooms'])
    distance =  int(request.form['distance'])
    prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'A house with {rooms} rooms located {distance} km from employment centers has a value of ${output}K.')

if __name__ == "__main__":
    app.run()

