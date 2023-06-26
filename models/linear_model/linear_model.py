from sklearn import linear_model
import pandas as pd
import numpy as np
import pickle
import logging
import os


# dir paths
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(script_dir, '..', '..'))
datasets_dir = os.path.join(base_dir, 'datasets')
logs_dir = os.path.join(base_dir, 'logs')


#file paths
in_file = os.path.join(datasets_dir, 'prices.csv') #dataset file
out_file = os.path.join(script_dir, 'linear_model.pkl') # model
log_file = os.path.join(logs_dir, 'app.log') # logs


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