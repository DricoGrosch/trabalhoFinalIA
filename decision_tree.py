import pandas
import seaborn as seaborn
from matplotlib import pyplot
from sklearn import tree
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier


class DecisionTree(DecisionTreeClassifier):
    dataset = None
    dataframe = None

    def set_dataset(self, dataset):
        self.dataset = dataset
        self.build_dataframe()

    def export_dataframe(self):
        self.dataframe.to_excel("output.xlsx")

    def build_dataframe(self):
        self.dataframe = pandas.DataFrame(data=self.dataset.data, columns=self.dataset.feature_names)
        self.dataframe['target'] = self.dataset.target
        self.dataframe['target names'] = pandas.Categorical.from_codes(self.dataset.target, self.dataset.target_names)

    def get_target_names(self):
        return self.dataset.target_names

    def get_features(self):
        return self.dataset.feature_names

    def train(self):
        # # x são as caracteristicas que tu quer informar pra saber se é maligno ou benigno. Ex: raio, textura, area. São as colunas do dataset
        feature_data = self.dataset.data
        # # valor alvo(rótulo). vai ser 0 ou 1 se for maligno ou benigno
        target = self.dataset.target
        # agora precisamos separar o datasets pra treino e pra teste
        #  o test size significa o quanto tu quer reservar pro teste. quanto maior o test size, mais preciso fica
        # random state é a aleatoriedade na divisão. serve pra não ficar um conjunto com com maligno e outro só com benigno, por exemplo
        self.train_features, self.test_features, self.target_train, self.target_test = train_test_split(feature_data,
                                                                                                        target,
                                                                                                        test_size=0.3,
                                                                                                        random_state=43)
        print(f'Train shape: {self.train_features.shape}')
        print(f'Test shape: {self.test_features.shape}')
        self.fit(self.train_features, self.target_train)

    def get_propabilities(self):
        return self.predict_proba(self.test_features)

    def get_predictions(self):
        'me diz a probabilidade de ser benigno e maligno para cada linha (y)'
        return self.predict(self.test_features)

    def get_confusion_matrix(self):
        return confusion_matrix(self.target_test, self.get_predictions(), labels=[0, 1])

    def get_accuracy_score(self):
        return accuracy_score(self.target_test, self.get_predictions())

    def get_precision_score(self):
        return precision_score(self.target_test, self.get_predictions())

    def get_recall_score(self):
        # O recall é a fração de casos raros corretamente previstos pelo modelo, em relação ao número
        # total de casos raros do nosso conjunto de dados. A precision é a fração de casos raros corretamente
        # previstos pelo modelo, em relação ao número total de previsões de casos raros. As seguintes
        # equações representam estas duas medidas.
        return recall_score(self.target_test, self.get_predictions())

    def get_feature_importance(self):
        return pandas.DataFrame(self.feature_importances_, index=self.dataset.feature_names).sort_values(0,
                                                                                                         ascending=False)

    def plot_feature_importance(self, feature_importance, kind):
        feature_importance.head(len(self.dataset.feature_names)).plot(kind=kind)
        pyplot.savefig('feature_importance.png')

    def plot_decision_tree(self):
        pyplot.figure(figsize=[25, 25])
        tree.plot_tree(self, feature_names=self.dataset.feature_names, class_names=self.dataset.target_names,
                       filled=True,
                       fontsize=8)
        pyplot.savefig('tree.png')
    def cross_validate(self):
        # cv é o iterador, como se fosse o I do for. nesse caso vai executar 10 vezes e calcular a acuracia de cada uma
        return cross_val_score(self, self.dataset.data, self.dataset.target, cv=5,scoring='accuracy'),
