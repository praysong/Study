import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense,Dropout,BatchNormalization, AveragePooling1D, Flatten, Conv2D, LSTM, Bidirectional,Conv1D,MaxPooling1D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler, Normalizer, RobustScaler
from sklearn.metrics import accuracy_score, f1_score
from keras.utils import to_categorical
import lightgbm as lgb
# 데이터 로드
# 데이터 로드
path = "c:\_data\dacon\dechul\\"
train_csv = pd.read_csv(path + "train.csv", index_col=0)
test_csv = pd.read_csv(path + "test.csv", index_col=0)
sample_csv = pd.read_csv(path + "sample_submission.csv")
x= train_csv.drop(['대출등급','최근_2년간_연체_횟수','총연체금액','연체계좌수'],axis=1)
y= train_csv['대출등급']
test_csv = test_csv.drop(['최근_2년간_연체_횟수','총연체금액','연체계좌수'],axis=1)
# 범주형 변수 리스트
categorical_cols = ['대출기간', '근로기간', '주택소유상태', '대출목적']

# 범주형 변수들을 정수로 인코딩
lb=LabelEncoder()
lb.fit(x['대출기간'])
x['대출기간'] = lb.transform(x['대출기간'])
lb.fit(x['근로기간'])
x['근로기간'] = lb.transform(x['근로기간'])
lb.fit(x['주택소유상태'])
x['주택소유상태'] = lb.transform(x['주택소유상태'])
lb.fit(x['대출목적'])
x['대출목적'] = lb.transform(x['대출목적'])

lb.fit(test_csv['대출기간'])
test_csv['대출기간'] =lb.transform(test_csv['대출기간'])

lb.fit(test_csv['근로기간'])
test_csv['근로기간'] =lb.transform(test_csv['근로기간'])

lb.fit(test_csv['주택소유상태'])
test_csv['주택소유상태'] =lb.transform(test_csv['주택소유상태'])

lb.fit(test_csv['대출목적'])
test_csv['대출목적'] =lb.transform(test_csv['대출목적'])

# 불필요한 컬럼 제거
x = train_csv.drop(['대출등급', '최근_2년간_연체_횟수', '총연체금액', '연체계좌수'], axis=1)
y = train_csv['대출등급']

y=y.values.reshape(-1,1)

ohe = OneHotEncoder(sparse=False)
ohe = OneHotEncoder()
y_ohe = ohe.fit_transform(y).toarray()

x_train,x_test,y_train,y_test=train_test_split(x,y_ohe,train_size=0.8,random_state=3 ,
                                               stratify=y
                                               )
# print(x_train.shape,x_test.shape)
# print(y_train.shape,y_test.shape)



# LightGBM 데이터셋 생성
train_data = lgb.Dataset(x, label=y, categorical_feature=categorical_cols)
valid_data = lgb.Dataset(x_test, label=y_test, reference=train_data, categorical_feature=categorical_cols)

# LightGBM 모델 설정
params = {
    'objective': 'multiclass',
    'num_class': 7,  # 클래스 개수
    'boosting_type': 'gbdt',
    'metric': 'multi_logloss',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

# LightGBM 모델 훈련
num_round = 100  # 반복 횟수
bst = lgb.train(params, train_data, num_boost_round=num_round, valid_sets=[valid_data])

# 나머지 코드는 그대로 사용
# LightGBM 모델 예측
y_pred = bst.predict(x_test, num_iteration=bst.best_iteration)
y_pred_class = [round(x) for x in y_pred]

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred_class)
f1 = f1_score(y_test, y_pred_class, average='macro')

print(f"Validation Accuracy: {accuracy}")
print(f"F1 Score: {f1}")

# 결과 예측
y_submit = bst.predict(test_csv, num_iteration=bst.best_iteration)
y_submit_class = [round(x) for x in y_submit]

# 예측 결과 저장
sample_csv["대출등급"] = y_submit_class
sample_csv.to_csv(path + "대출_lgbm.csv", index=False)

