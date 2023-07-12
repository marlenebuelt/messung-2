import pandas as pd
import pickle
import time
import logging


def predictX(clf, X_test):
    predicted = clf.predict(X_test)
    return predicted

logging.basicConfig(filename="/home/marlene/messungen_64bit/3_svm/svm.log", 
					format='%(asctime)s %(message)s', 
					filemode='a',
                    level=logging.DEBUG) 
logger=logging.getLogger()

for i in range (30):
    logger.info("Start") 
    svm_model = pickle.load(open('Modelle/03_svm/SVMmodel_3months.pkl', 'rb'))
    X_test_svm = pickle.load(open('Modelle/03_svm/X_test_3months.pkl', 'rb'))
    predicted = predictX(svm_model, X_test_svm) 
    logger.info("Stop")
    time.sleep(10)
