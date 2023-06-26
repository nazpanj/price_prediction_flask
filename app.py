from flask import Flask, render_template, request
import pickle
import logging
import os

# paths
in_file = "models/linear_model/linear_model.pkl"  #model file
log_file = "logs/app.log"

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

