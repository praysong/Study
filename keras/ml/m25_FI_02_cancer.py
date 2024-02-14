import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
import time
from sklearn.datasets import load_breast_cancer
#1. 데이터
datasets= load_breast_cancer()

x = datasets.data       #(569, 30)
y = datasets.target     #(569,)

feature_names = datasets.feature_names
# x=x[:,6:]
# x = pd.DataFrame(x, columns=feature_names)

# 첫 번째 열 삭제
# x = x.drop(columns=[feature_names[0]])
# print(x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8,
                                                    random_state=1,         #850:acc=1
                                                    stratify=y              #stratify는 분류에서만 사용
                                                    )
from xgboost import XGBClassifier


allAlgorithms = [
    ('LogisticRegression', XGBClassifier),
    ('KNeighborsClassifier',GradientBoostingClassifier),
    ('DecisionTreeClassifier', DecisionTreeClassifier),
    ('RandomForestClassifier', RandomForestClassifier)
]
# 피쳐 임포턴스를 사용하여 하위 25%의 피쳐를 선택하는 함수
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
    x_train_selected = x_train[:, [feature_names.tolist().index(feature) for feature in selected_feature_names]]
    x_test_selected = x_test[:, [feature_names.tolist().index(feature) for feature in selected_feature_names]]
    # 모델 재훈련
    model.fit(x_train_selected, y_train)
    # 모델 평가
    acc = model.score(x_test_selected, y_test)
    print(f"{algorithm.__name__}'s 정확도 (하위 25% 피쳐 선택):", acc)

# 각 알고리즘에 대해 피쳐 임포턴스를 사용하여 하위 25%의 피쳐를 선택하여 모델을 훈련/평가
for name, algorithm in allAlgorithms:
    train_and_evaluate_with_feature_selection(algorithm, x_train, y_train, x_test, y_test, feature_names)

for name, algorithm in allAlgorithms:
    model = algorithm()
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(name, '의 정확도:', acc)

'''
XGBClassifier's 정확도 (하위 25% 피쳐 선택): 0.9122807017543859
GradientBoostingClassifier's 정확도 (하위 25% 피쳐 선택): 0.9210526315789473
DecisionTreeClassifier's 정확도 (하위 25% 피쳐 선택): 0.9298245614035088
RandomForestClassifier's 정확도 (하위 25% 피쳐 선택): 0.9210526315789473
LogisticRegression 의 정확도: 0.9824561403508771
KNeighborsClassifier 의 정확도: 0.9649122807017544
DecisionTreeClassifier 의 정확도: 0.9385964912280702
RandomForestClassifier 의 정확도: 0.956140350877193
'''
    