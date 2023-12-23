import pandas as pd
import pickle
from tensorflow.keras.models import load_model
import time
import logging

def predictX(clf, X_test):
    predicted = clf.predict(X_test, verbose=0)
    return predicted

formatter = logging.Formatter('%(asctime)s %(message)s')

def setup_logger(name, log_file, level=logging.DEBUG):
 
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger_fullLoops = setup_logger('logger_fullLoops', "/home/marlene/messungen/2_logreg/lr_fullLoops_logs.log")
logger_singleLoops = setup_logger('logger_singleLoops', '/home/marlene/messungen/2_logreg/lr_singleLoops_logs.log')


for i in range (30):
    logger_fullLoops.info("Start")
    for i in range (10):
        logger_singleLoops.info("Start")
        nn_model = load_model('04_nn/nn_3months/')
        X_test_nn = pickle.load(open('04_nn/X_test_3months.pkl', 'rb'))
        predicted = nn_model.predictX(nn_model, X_test_nn)
        logger_singleLoops.info("Stop")
        time.sleep(10)
    logger_fullLoops.info("Stop")
