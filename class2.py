import numpy as np
from sklearn.datasets import make_classification
x,y=make_classification(n_samples=1000,n_features=20,n_informative=10,n_classes=2,random_state=42)
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV
paran_dist={
    "max_depth":[3,None],
    "max_features":randint(4,9),
    "min_samples_leaf":randint(1,6),
    "criterion":["gini","entropy"]

}
tree=DecisionTreeClassifier()
tree_cv=RandomizedSearchCV(tree,paran_dist,cv=5)
tree_cv.fit(x,y)
print("tuned decision tree parameaters:{}",format(tree_cv.best_params_))
print("best score is{}",format(tree_cv.best_score_))