import pandas as pd
import pickle
from tensorflow.keras.models import load_model
import time
import logging

logging.basicConfig(filename="/home/marlene/messungen_64bit/04_nn_results/nn.log", 
					format='%(asctime)s %(message)s', 
					filemode='a',
                    level=logging.DEBUG) 
logger=logging.getLogger()


for i in range (30):
    logger.info("Start") 
    nn_model = load_model('Modelle/04_nn/nn_3months')
    X_test_nn = pickle.load(open('Modelle/04_nn/X_test_3months.pkl', 'rb'))
    predicted = nn_model.predict(X_test_nn)
    logger.info("Stop")
    time.sleep(10)
