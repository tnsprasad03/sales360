"""
Description: Validate Model class and generate scores.
"""

import numpy as np
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import metrics

class ModelValidation(object):
    """
    A class to validate model
    """
    def __init__(self):
        self.features = [] # list of features
        self.impfeatures = []  # list of important features
        
        

    def get_score(self, clf,X,y):
        scores = cross_validation.cross_val_score(clf, X, y, cv=5)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
        print "%s -- %s" % (clf.__class__, np.mean(scores))
        

        #fit and predict model
        clf.fit(X_train, y_train)

        #gather predict probas to evaluate scores

        probas_ = clf.predict_proba(X_test)
        y_pred = clf.predict(X_test)


        fpr, tpr,thresholds = roc_curve(y_test, probas_[:, 1]) 
        roc_auc = auc(fpr, tpr)

        # Print scores for the requested model for analysis.
        print("Area under the ROC curve : %f" % roc_auc)
        print "precision of model", metrics.precision_score(y_test, y_pred, average='weighted')
        print "f score of model", metrics.f1_score(y_test, y_pred, average='weighted') 
        print "recall of model", metrics.recall_score(y_test, y_pred, average='weighted')

        return clf


