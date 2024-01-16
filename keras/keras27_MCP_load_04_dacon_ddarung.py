# https://dacon.io/competitions/open/235576/leaderboard

from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from keras.models import Sequential,load_model
from keras.layers import Dense
import numpy as np
import pandas as pd

#1. 데이터

path= "c:\_data\dacon\ddarung\\"
# print(path+ "aaa.csv")      #c:\_data\dacon\ddarung\aaa.csv
# train_csv = pd.read_csv("c:/_data/dacon/ddarung//train.csv")
# test_csv= pd.read_csv("c:/_data/dacon/ddarung//test.csv")
# submission_scv= pd.read_csv("c:/_data/dacon/ddarung//submission.csv")
train_csv = pd.read_csv(path+"train.csv",index_col=0)
test_csv= pd.read_csv(path+"test.csv",index_col=0)
submission_csv= pd.read_csv(path+"submission.csv")

# train_csv = train_csv.dropna()
train_csv=train_csv.fillna(train_csv.mean())                         #test는 dropna를 하면 안되고 결측치를 변경해줘야한다
# train_csv=train_csv.fillna(0)
test_csv=test_csv.fillna(test_csv.mean())                         #test는 dropna를 하면 안되고 결측치를 변경해줘야한다
# test_csv=test_csv.fillna(0)


#######x와 y분리#######
x= train_csv.drop(['count'],axis=1)
y= train_csv['count']


#####결측치확인######
# print(train_csv.isna().sum())         isna 어디에 nan값이 있나
# print(train_csv.isna().sum())
# print(train_csv.info())
# print(train_csv.shape)      (1328, 10)


x_train,x_test,y_train,y_test=train_test_split(x,y, train_size=0.8, random_state=6)

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
scaler = MaxAbsScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# #2. 모델구성
# model=Sequential()
# model.add(Dense(15,input_dim=9))
# model.add(Dense(20))
# model.add(Dense(100))
# model.add(Dense(150))
# model.add(Dense(80))
# model.add(Dense(40))
# model.add(Dense(10))
# model.add(Dense(1))



# #3.컴파일,훈련
# from keras.callbacks import EarlyStopping, ModelCheckpoint
# mcp = ModelCheckpoint(
#     monitor='val_loss',
#     mode='auto',
#     verbose=1,
#     save_best_only=True,
#     filepath='..\_data\_save\MCP\keras26_MCP_dacon_ddarung.hdf5'
#     )
# es= EarlyStopping(monitor='val_loss',mode='min',patience=100,verbose=1,restore_best_weights=True)
# model.compile(loss='mse',optimizer='adam')
# hist= model.fit(x_train, y_train, epochs=1000,batch_size=1000, validation_split=0.1,verbose=2,
#           callbacks=[es,mcp])

# model.save("c:\_data\_save\dacon_ddarung_1.h5")

model = load_model("c:\_data\_save\\dacon_ddarung_1.h5")

model.summary()
#4.결과예측
loss = model.evaluate(x_test,y_test)
y_submit=model.predict(test_csv)

submission_csv['count'] = y_submit
# print(submission_csv)
submission_csv.to_csv(path + "submission_21.csv", index=False)
print("로스 :",loss)

'''
로스 : 2618.900634765625

'''