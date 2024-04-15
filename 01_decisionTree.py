import pandas as pd
import pickle
import time
import logging

#logs: credit to https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings
def predictX(clf, X_test):
    predicted = clf.predict(X_test)
    return predicted

formatter = logging.Formatter('%(asctime)s %(message)s')

def setup_logger(name, log_file, level=logging.DEBUG):
 
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger_fullLoops = setup_logger('logger_fullLoops', "/home/marlene/messungen/1_dt_results/dte_fullLoops_logs.log")
logger_singleLoops = setup_logger('logger_singleLoops', '/home/marlene/messungen/1_dt_results/dte_singleLoops_logs.log')

for i in range (30):
    logger_fullLoops.info("Start")
    for i in range (10):
        logger_singleLoops.info("Start")
        DTE_model = pickle.load(open('01_decisionTree/Decisiontreemodel_3months.pkl', 'rb'))
        X_test_DTE = pickle.load(open('01_decisionTree/X_test_3months.pkl', 'rb'))
        predicted = predictX(DTE_model, X_test_DTE)
        logger_singleLoops.info("Stop")
        time.sleep(10)
    logger_fullLoops.info("Stop") 
    
