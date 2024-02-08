import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import Perceptron,LogisticRegression,SGDClassifier
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.utils import all_estimators
import warnings
warnings.filterwarnings('ignore')
# 1.데이터
datasets = load_iris()
df=pd.DataFrame(datasets.data,columns=datasets.feature_names)
print(df)


# x,y = load_iris(return_X_y=True)
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8,
#                                                     random_state=450,         #850:acc=1
#                                                     stratify=y              #stratify는 분류에서만 사용
#                                                     )
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import StratifiedKFold
n_split = 3
kfold = KFold(n_splits=n_split,shuffle=True, random_state=123)
print("--------------------------------------")
for train_index, val_index in kfold.split(df):
    print(train_index,"\n",val_index)
    print("훈련데이터의갯수",len(train_index),"검증데이터의갯수",len(val_index))
# from sklearn.model_selection import StratifiedKFold
# kfold = StratifiedKFold(n_splits=n_split,shuffle=True, random_state=123)

# #2.모델
# model = SGDClassifier()   #소프트벡터머신 클래스파이어
# #3.훈련
# scores = cross_val_score(model,x,y,cv=kfold)

# print("ACC:",scores,"\n 평균:",round(np.mean(scores),4))
# '''
# CC: [0.86666667 1.         0.83333333 0.56666667 0.63333333] 
#  평균: 0.78
# '''