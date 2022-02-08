from sklearn.datasets import load_breast_cancer

from decision_tree import DecisionTree

decision_tree = DecisionTree(criterion='entropy')
decision_tree.set_dataset(load_breast_cancer())
decision_tree.build_dataframe()
print(f'Features: {decision_tree.get_features()}')
print(f'Target Names: {decision_tree.get_target_names()}')
decision_tree.export_dataframe()
decision_tree.train()
scores = decision_tree.cross_validate()
print(f'scores: {scores}')
print(f"Cross validation Score Mean: {scores.mean()}")
print(f"Cross validation standart deviation: {scores.std()}")
print(f'Prediction: {decision_tree.get_predictions()}')
print(f'Probabilities: {decision_tree.get_propabilities()}')
print(f'Accuracy: {decision_tree.get_accuracy_score()}')
print(f'Confusion Matrix: {decision_tree.get_confusion_matrix()}')
print(f'Precision: {decision_tree.get_precision_score()}')
print(f'Recall: {decision_tree.get_recall_score()}')
decision_tree.plot_feature_importance(decision_tree.get_feature_importance(), 'bar')
decision_tree.plot_decision_tree()
