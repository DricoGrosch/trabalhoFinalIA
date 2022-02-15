import random

from numpy import mean, std
from sklearn.datasets import load_breast_cancer
from sklearn.tree import export_text

from decision_tree import DecisionTree


def get_best_values(criterion, max_depth, test_size):
    decision_tree = DecisionTree(criterion=criterion, max_depth=max_depth, dataset=load_breast_cancer(),
                                 test_size=test_size)
    decision_tree.train()
    acc = decision_tree.get_accuracy_score()
    prec = decision_tree.get_precision_score()
    rec = decision_tree.get_recall_score()
    f1 = decision_tree.get_f1_score()

    return acc, prec, rec, f1


best_acc = 0
best_prec = 0
best_rec = 0
best_f1 = 0
best_max_depth = 0
best_test_size = 0
best_method = ''
for depth in range(1, 100):
    for _test_size in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        print(_test_size)
        print(depth)
        acc, prec, rec, f1 = get_best_values('entropy', depth, _test_size)
        if acc > best_acc and prec > best_prec and rec > best_rec and f1 > best_f1:
            best_acc = acc
            best_prec = prec
            best_rec = rec
            best_f1 = f1
            best_max_depth = depth
            best_test_size = _test_size
            best_method = 'entropy'

for depth in range(1, 100):
    for _test_size in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        print(_test_size)
        print(depth)
        acc, prec, rec, f1 = get_best_values('gini', depth, _test_size)
        if acc > best_acc and prec > best_prec and rec > best_rec and f1 > best_f1:
            best_acc = acc
            best_prec = prec
            best_rec = rec
            best_f1 = f1
            best_max_depth = depth
            best_test_size = _test_size
            best_method = 'gini'

print(f'best_f1 {best_f1}')
print(f'best_max_depth {best_max_depth}')
print(f'best_test_size {best_test_size}')
print(f'best_method  {best_method}')
