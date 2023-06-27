# Price Prediction Web App
This is a machine learning web application that utilizes a linear model to predict house prices based on number of rooms and distance from employment centers
[Price Prediction Web App Tutorial](https://www.youtube.com/watch?v=O6BB08Zo2uk)

## Project Structure

The project is organized into the following directories and files:

- `app.py`: This file contains the main application code, including the route handlers.
- `templates/`: This directory contains HTML templates used in the web app.
- `models/`: This directory contains the implementation of machine learning models.
  - `models/linear_model/`: Directory specifically for the linear model implementation.
- `datasets/`: This directory contains the datasets used by the machine learning models.
- `logs/`: This directory contains application logs.


## Getting Started

These instructions will help you set up and run the web app on your local machine.

1. Clone the repository:
```bash
git clone git@github.com:nazpanj/price_prediction_flask.git
```

2. Navigate to dir:  
```bash
cd price_prediction_flask
```

3. Create a conda environment and install the requirements:  
```bash
conda create --name your_env_name --file requirements.txt
```

4. Activate the conda environment (macOS):  
```bash
conda activate your-env-name
```

5. Navigate to dir:
```bash
cd models/linear_model
```

6. Run the file:
```bash
python linear_model.py
```
* this will train the model using the `datasets/price.csv`
* the trained model will be saved as `models/linear_model/linear_model.pkl`

7. Navigate to project dir and run the application
```bash
python app.py
```

8. The above command will start your Flask application and it will be accessible at:  `http://localhost:5000`

9. Use the web interface:
- Enter the number of rooms
- Enter the distance
- Click on Predict Value button to get the predicted value


## Dependencies
The project's dependencies are listed in the requirements.txt file. They include:

- Flask: A micro web framework for building web applications. 
- Data science libraries such as scikit-learn, numpy, pandas, etc.