import pandas as pd
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import pickle

df = pd.read_csv("PhishingData.txt")

print(df.columns)

columnLabel = preprocessing.LabelEncoder()
results =  columnLabel.fit_transform(df["Result"])
x = df[["SFH", "popUpWidnow", "SSLfinal_State", "Request_URL", "URL_of_Anchor", "web_traffic", "URL_Length", "age_of_domain", "having_IP_Address"]]
y = results


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

def trainModel():
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    phishingModel = KNeighborsClassifier(n_neighbors=3)
    phishingModel.fit(x, y)

    best_score = 0.97

    modelAccuracy = phishingModel.score(x_test, y_test)

    if modelAccuracy > best_score:
        print(modelAccuracy)

        with open("phishing-model.pickle", "wb") as f:
            pickle.dump(phishingModel, f)


def runTrain():
    for _ in range(50):
        trainModel()


def testModel():
    phishing_model = open("phishing-model.pickle", "rb")
    trainedModel = pickle.load(phishing_model)

    predictions = trainedModel.predict(x_test)
    names = ["Legitimate", "Suspicious", "Phishy"]

    for x in range(len(x_test)):
        print("Prediction: ", names[predictions[x]], " ---> ", "Actual value: ", names[y_test[x]])
    
    '''for x in range(len(predictions)):
        print(names[predictions[x]])'''


#runTrain()
testModel()