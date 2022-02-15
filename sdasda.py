import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# MLP Classifier
from sklearn.neural_network import MLPClassifier
# Metrics

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Confusion Matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, f1_score

from sklearn.neural_network import MLPClassifier

# TODO review
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder, StandardScaler

import pickle
import os.path


def read_saved_classifier():
    file_exists = os.path.exists(CLASSIFIER_FILE)

    if not file_exists:
        return None

    with open(CLASSIFIER_FILE, 'rb') as fid:
        return pickle.load(fid)


def save_classifier(classifier):
    with open(CLASSIFIER_FILE, 'wb') as fid:
        pickle.dump(classifier, fid)

    # arg: test_size: define a porcentagem dos dados totais do dataset que serão usados para teste


#
# ex.: com test_size: 0.2: 80% do dataset será usado para treinamento (x_train), e o restante (20%)
# será reservado para ser usado no teste (x_test)
#
# x_train (dados para treino)
# y_train (objetivos para treino)
# x_test (dados para teste)
# y_test (objetivos para teste)
TEST_SIZE = 0.2

CLASSIFIER_FILE = 'classifier.pkl'


def read_dataset():
    return pd.read_csv('csgo_round_snapshots.csv', delimiter=',')


def preprocess_dataset(dataset):
    # Precisamos usar o LabelEncoder para mapear a coluna 'map' para valores numéricos
    # ex.: {'de_dust2' -> 01; 'de_mirage' -> 02; etc}
    label_encoder = LabelEncoder()
    label_encoder.fit(dataset['map'])
    dataset['map'] = label_encoder.transform(dataset['map'])

    # para definir x, precisamos  ler todas as colunas, menos a última
    # pois a última coluna ('round_winner') armazena o resultado de cada rodada
    x = dataset[dataset.columns[:-1]]

    # TODO review
    x = StandardScaler().fit_transform(x)

    # resultado de qual time (CT ou TR) venceu a rodada
    y = dataset['round_winner']

    return x, y


# essa função vai retornar um classifier treinado
def run_training(x_train, y_train):
    max_iter = x_train.shape[0]

    mlp_classifier = MLPClassifier(max_iter=max_iter).fit(x_train, y_train)

    return mlp_classifier



def build_metrics(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average='binary')
    f1 = f1_score(y_test, y_pred, average='binary')

    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    specificity = tn / (tn + fp)

    return (accuracy, precision, recall, specificity, f1)


def print_metrics(metrics):
    print('print_metrics')


classifier = read_saved_classifier()

# não existe classifier previamente treinado, portanto, executa a rotina de treino
if classifier is None:
    dataset = read_dataset()
    x, y = preprocess_dataset(dataset)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE)
    classifier = run_training(x_train, y_train)
    save_classifier(classifier)

y_pred = classifier.predict(x_test)
metrics = build_metrics(y_test, y_pred)
print_metrics(metrics)