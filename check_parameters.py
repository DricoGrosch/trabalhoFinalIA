import random

from numpy import mean, std
from sklearn.datasets import load_breast_cancer
from sklearn.tree import export_text

from decision_tree import DecisionTree


def get_best_values(criterion, max_depth, test_size):
    decision_tree = DecisionTree(criterion=criterion, max_depth=max_depth, dataset=load_breast_cancer(),
                                 test_size=test_size)
    decision_tree.export_dataframe()
    decision_tree.train()
    return decision_tree.get_f1_score()


best_f1 = 0
best_max_depth = 0
best_test_size = 0
best_method = ''
for i in range(100):
    max_depth = round(random.uniform(1, 100),1)
    test_size = round(random.uniform(0.1, 0.9),2)
    f1 = get_best_values('entropy', max_depth, test_size)
    if f1 > best_f1:
        best_f1 = f1
        best_max_depth = max_depth
        best_test_size = test_size
        best_method = 'entropy'

for i in range(100):
    max_depth = round(random.uniform(1, 100),1)
    test_size = round(random.uniform(0.1, 0.9),2)
    f1 = get_best_values('gini', max_depth, test_size)
    if f1 > best_f1:
        best_f1 = f1
        best_max_depth = max_depth
        best_test_size = test_size
        best_method = 'gini'
print(f'best_f1 {best_f1}')
print(f'best_max_depth {best_max_depth}')
print(f'best_test_size {best_test_size}')
print(f'best_method  {best_method }')