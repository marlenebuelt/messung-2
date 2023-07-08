import pandas as pd
import pickle
import time
import logging

def predictX(clf, X_test):
    predicted = clf.predict(X_test)
    return predicted

logging.basicConfig(filename="/home/marlene/messungen_64bit/1_dt_results/dte.log", 
					format='%(asctime)s %(message)s', 
					filemode='a',
                    level=logging.DEBUG) 
logger=logging.getLogger()

for i in range (30):
    logger.info("Start")
    DTE_model = pickle.load(open('Modelle/01_decisionTree/Decisiontreemodel_3months.pkl', 'rb'))
    X_test_DTE = pickle.load(open('Modelle/01_decisionTree/X_test_3months.pkl', 'rb'))
    predicted = predictX(DTE_model, X_test_DTE)
    logger.info("Stop") 
    time.sleep(10)
    
    
