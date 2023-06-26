from sklearn import linear_model
import pandas as pd
import numpy as np
import pickle
import logging
import os


# paths
in_file = "datasets/prices.csv" #dataset
out_file = "models/linear_model/linear_model.pkl" #model
log_file = "logs/app.log"

# configure logs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', filename=log_file, filemode='a')

# current running file
logging.info("Running file %s", os.path.basename(__file__))

# read the file 
logging.info("Reading data from %s", in_file)
df = pd.read_csv(in_file)
logging.info(df.head())

y = df['Value']
X = df.iloc[:,0:2].values 

# call the model
logging.info("Training the model")
lm = linear_model.LinearRegression()
lm.fit(X,y)

# save the trained model
logging.info("Saving the model %s", out_file)
with open(out_file, 'wb') as f:
    pickle.dump(lm, f)

logging.info(lm.predict([[15, 61]]))
logging.info(f'score: {lm.score(X,y)}')