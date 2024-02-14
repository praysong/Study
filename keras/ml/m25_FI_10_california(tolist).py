import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,GradientBoostingRegressor
from sklearn.datasets import fetch_california_housing

#1.데이터
datasets = fetch_california_housing()
x =datasets.data
y =datasets.target
feature_names = datasets.feature_names

# print(x)   #(20640, 8)
# print(y)   #(20640,)
# print(x.shape,y.shape)
#print(datasets.feature_names)  #['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
x= x[:,2:]

from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=130)
#2. 모델구성
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, RobustScaler
scaler = RobustScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

from xgboost import XGBRegressor


allAlgorithms = [
    ('LogisticRegression', XGBRegressor),
    ('KNeighborsClassifier',GradientBoostingRegressor),
    ('DecisionTreeClassifier', DecisionTreeRegressor),
    ('RandomForestClassifier', RandomForestRegressor)
]
def select_features_with_importance(model, x_train, feature_names):
    # 모델 피쳐 임포턴스 추출
    feature_importances = model.feature_importances_
    # 피쳐 중요도 기준으로 정렬
    sorted_indices = np.argsort(feature_importances)
    # 하위 25%의 피쳐 인덱스 선택
    num_features_to_keep = int(len(feature_names) * 0.25)  # 상위 75% 선택
    selected_indices = sorted_indices[num_features_to_keep:]
    # 선택된 피쳐 이름 반환
    selected_feature_names = [feature_names[i] for i in selected_indices]
    return selected_feature_names

# 피쳐 임포턴스를 사용하여 하위 25%의 피쳐를 선택하여 모델을 훈련/평가하는 함수
# 피쳐 임포턴스를 사용하여 하위 25%의 피쳐를 선택하여 모델을 훈련/평가하는 함수
def train_and_evaluate_with_feature_selection(algorithm, x_train, y_train, x_test, y_test, feature_names):
    # 모델 생성
    model = algorithm()
    # 모델 훈련
    model.fit(x_train, y_train)
    # 선택된 피쳐들을 추출
    selected_feature_names = select_features_with_importance(model, x_train, feature_names)
    if len(selected_feature_names) == 0:
        print("선택된 피쳐가 없습니다.")
        return
    # 선택된 피쳐들을 이용하여 새로운 데이터셋 생성
    x_train_selected = x_train[:, [feature_names.index(feature) for feature in selected_feature_names]]
    x_test_selected = x_test[:, [feature_names.index(feature) for feature in selected_feature_names]]
    # 모델 재훈련
    model.fit(x_train_selected, y_train)
    # 모델 평가
    acc = model.score(x_test_selected, y_test)
    print(f"{algorithm.__name__}'s 정확도 (하위 25% 피쳐 제거):", acc)

# 각 알고리즘에 대해 피쳐 임포턴스를 사용하여 하위 25%의 피쳐를 선택하여 모델을 훈련/평가
for name, algorithm in allAlgorithms:
    train_and_evaluate_with_feature_selection(algorithm, x_train, y_train, x_test, y_test, feature_names)

for name, algorithm in allAlgorithms:
    model = algorithm()
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(name, '의 정확도:', acc)
'''
XGBRegressor's 정확도 (하위 25% 피쳐 선택): 0.8074385342381346
GradientBoostingRegressor's 정확도 (하위 25% 피쳐 선택): 0.7274102554438612
DecisionTreeRegressor's 정확도 (하위 25% 피쳐 선택): 0.6431031900829585
RandomForestRegressor's 정확도 (하위 25% 피쳐 선택): 0.8063785088299034
LogisticRegression 의 정확도: 0.8146686419969025
KNeighborsClassifier 의 정확도: 0.7412643329851862
DecisionTreeClassifier 의 정확도: 0.6449588912288873
RandomForestClassifier 의 정확도: 0.8101390141291306
'''