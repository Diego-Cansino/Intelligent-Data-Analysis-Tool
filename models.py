from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

def getDecisionTree():
    return DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, criterion='entropy', min_samples_split=5,
                                       splitter='random', random_state=1)
                                    
def getKNN():
    return KNeighborsClassifier(n_neighbors=8)

def getLogisticRegression():
    return LogisticRegression(max_iter=1000, random_state=1, solver='liblinear', penalty='l1')

def getANN():
    return MLPClassifier(hidden_layer_sizes=(10,15), activation='logistic', solver='adam', max_iter=500, random_state=1)