import pandas as pd
import pickle
import time
import logging

def predictX(clf, X_test):
    predicted = clf.predict(X_test)
    return predicted

logging.basicConfig(filename="/home/marlene/messungen_64bit/2_logreg/logreg.log", 
					format='%(asctime)s %(message)s', 
					filemode='a',
                    level=logging.DEBUG) 
logger=logging.getLogger()

for i in range (30):
    logger.info("Start")
    logreg_model = pickle.load(open('Modelle/02_logisticRegression/Logregmodel_3months.pkl', 'rb'))
    X_test_logreg = pickle.load(open('Modelle/02_logisticRegression/X_test_3months.pkl', 'rb'))
    predicted = predictX(logreg_model, X_test_logreg)
    logger.info("Stop")
    time.sleep(10)
  
