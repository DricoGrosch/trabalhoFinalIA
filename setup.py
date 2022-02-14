from distutils.core import setup # Need this to handle modules
import py2exe
from numpy import mean, std
from sklearn.datasets import load_breast_cancer
from sklearn.tree import export_text

from decision_tree import DecisionTree
setup(console=['main.py'])