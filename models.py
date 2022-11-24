from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression, BayesianRidge
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB

# classification models #

def getDecisionTree():
    return DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, criterion='entropy', min_samples_split=5,
                                       splitter='random', random_state=1)
                                    
def getKNN():
    return KNeighborsClassifier(n_neighbors=8)

def getLogisticRegression():
    return LogisticRegression(max_iter=1000, random_state=1, solver='liblinear', penalty='l1')

def getANN():
    return MLPClassifier(hidden_layer_sizes=(10,15), activation='logistic', solver='adam', max_iter=500, random_state=1)

def getSVMClassifier():
    return SVC()

def getNaiveBayes():
    return GaussianNB()

# regression models #

def getDecisionTreeRegression():
    return DecisionTreeRegressor(random_state=0)

def getKNNRegression():
    return KNeighborsRegressor(8)

def getLinearRegression():
    return LinearRegression()

def getANNRegression():
    return MLPRegressor(random_state=1, max_iter=500)

def getSVMRegression():
    return SVR()

def getBayesianRidge():
    return BayesianRidge()