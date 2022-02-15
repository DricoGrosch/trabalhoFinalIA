from numpy import mean, std
from sklearn.datasets import load_breast_cancer
from sklearn.tree import export_text

from decision_tree import DecisionTree

decision_tree = DecisionTree(criterion='entropy', max_depth=3, dataset=load_breast_cancer(), test_size=0.1)
print(f'Features: {decision_tree.get_features()}')
print(f'Target Names: {decision_tree.get_target_names()}')
decision_tree.export_dataframe()
decision_tree.train()
print(f'Prediction: {decision_tree.get_predictions()}')
print(f'Probabilities: {decision_tree.get_propabilities()}')
print(f'Accuracy: {decision_tree.get_accuracy_score()}')
print(f'Precision: {decision_tree.get_precision_score()}')
print(f'Recall: {decision_tree.get_recall_score()}')
print(f'F1 Score: {decision_tree.get_f1_score()}')
print(f'Confusion Matrix: {decision_tree.get_confusion_matrix()}')

scores = decision_tree.cross_validate()
print(f"scores: {scores}")
print(f"Cross validation Score Mean: {mean((scores))}")
print(f"Cross validation standart deviation: {std(scores)}")
print(decision_tree.get_feature_importance())
decision_tree.plot_feature_importance(decision_tree.get_feature_importance(), 'bar')
decision_tree.plot_decision_tree()
print(export_text(decision_tree, feature_names=decision_tree.dataset.feature_names.tolist()))
