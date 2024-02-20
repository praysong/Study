import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler, Normalizer, RobustScaler
from sklearn.metrics import accuracy_score, f1_score
from lightgbm import LGBMClassifier,Booster
import lightgbm as lgb
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV,HalvingGridSearchCV,HalvingRandomSearchCV,KFold

path= "c:/_data/kaggle/비만/"
train=pd.read_csv(path+"train.csv",index_col=0)
test=pd.read_csv(path+"test.csv",index_col=0)
sample=pd.read_csv(path+"sample_submission.csv")
x= train.drop(['NObeyesdad'],axis=1)
y= train['NObeyesdad']
# print(train.shape,test.shape)   #(20758, 17) (13840, 16)    NObeyesdad
# print(x.shape,y.shape)  #(20758, 16) (20758,)

lb = LabelEncoder()

# 라벨 인코딩할 열 목록
columns_to_encode = ['Gender','family_history_with_overweight','FAVC','CAEC','SMOKE','SCC','CALC','MTRANS']

# 데이터프레임 x의 열에 대해 라벨 인코딩 수행
for column in columns_to_encode:
    lb.fit(x[column])
    x[column] = lb.transform(x[column])

# 데이터프레임 test_csv의 열에 대해 라벨 인코딩 수행
for column in columns_to_encode:
    lb.fit(test[column])
    test[column] = lb.transform(test[column])

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, random_state=367, stratify=y,shuffle=True)

scaler =StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
test = scaler.transform(test)
import random
r1 = random.randint(400, 500)
r2 = random.randint(1, 100)
r3 = random.randint(1, 100)
r4 = random.randint(1, 100)
# r3 = random.randint(1, 100)
# r3 = random.randint(1, 100)
rs1 = np.linspace(0.1, 10, 1)
rs2 = np.linspace(0.1, 1, 1)
rs3 = np.linspace(0.1, 10, 1)
# rs4 = np.linspace(0.1, 10, 10)
# rs5 = np.linspace(0.1, 10, 10)

# 모델 생성 및 학습
params = {
            #    "objective": "multiclass",
            #    "metric": "multi_logloss",
               "verbosity": [-1,-2],
            #    "boosting_type": "gbdt",
            #    "random_state": random_state,
               "num_class": [7,8],
               "learning_rate": [0.0138643212125253,0.01386432121252535],
               "n_estimators": [r1],
            #    "feature_pre_filter": False,
               "lambda_l1": [1.2149501037669967e-06,1.2149501037669967e-07],
               "lambda_l2": [0.923089014319675,0.9230890143196759],
               "feature_fraction": [0.5],
               "bagging_fraction": [0.5523862448863431],
               "bagging_freq": [r2],
               "min_child_samples": [20],
               "max_depth":[r3],
               "min_samples_leaf":[r4],
               'reg_alpha' : [rs2],
               'reg_lambda': [rs3],
               'n_jobs': [-1]
               
               }


light = LGBMClassifier(**params,device='gpu')

n_split = 5
kfold = KFold(n_splits=n_split,shuffle=True, random_state=123)
model = HalvingRandomSearchCV(light,params, cv = kfold,verbose=1,refit=True,n_jobs=-1,random_state=6,factor=2,min_resources=10)

model.fit(x_train, y_train)

# 모델 저장
# booster = model.booster_
# model.booster_.save_model("c:/_data/_save/비만41.h5")
import pickle
pickle.dump(model, open(path + '비만41.dat1','wb'))

# 테스트 데이터 예측 및 저장
y_pred = model.predict(x_test)
y_submit = model.predict(test)
sample['NObeyesdad'] = y_submit
sample.to_csv(path + "비만41.csv", index=False)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("r1",r1)
print("r2",r2)
print("r3",r3)
print("r4",r4)
# print("r",rs1)
print("rs2",rs2)
print("rs3",rs3)

# print("사용파라미터",model.get_params())


