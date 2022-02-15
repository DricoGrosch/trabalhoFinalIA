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
for depth in range(1, 100):
    for _test_size in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        print(_test_size)
        print(depth)
        f1 = get_best_values('entropy', depth, _test_size)
        if f1 > best_f1:
            best_f1 = f1
            best_max_depth = depth
            best_test_size = _test_size
            best_method = 'entropy'

for depth in range(1, 100):
    for _test_size in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        print(_test_size)
        print(depth)
        f1 = get_best_values('gini', depth, _test_size)
        if f1 > best_f1:
            best_f1 = f1
            best_max_depth = depth
            best_test_size = _test_size
            best_method = 'gini'
print(f'best_f1 {best_f1}')
print(f'best_max_depth {best_max_depth}')
print(f'best_test_size {best_test_size}')
print(f'best_method  {best_method}')
