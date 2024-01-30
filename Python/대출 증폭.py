import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Dropout,BatchNormalization,LSTM,SimpleRNN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler, Normalizer, RobustScaler
from sklearn.metrics import accuracy_score, f1_score
from keras.utils import to_categorical
#1.데이터
path= "c:\_data\dacon\dechul\\"
train_csv=pd.read_csv(path+"train.csv",index_col=0)
test_csv=pd.read_csv(path+"test.csv",index_col=0)
sample_csv=pd.read_csv(path+"sample_submission.csv")
x= train_csv.drop(['대출등급'],axis=1)
y= train_csv['대출등급']


# print(train_csv,train_csv.shape)        (96294, 14)
# print(test_csv,test_csv.shape)          (64197, 13)
# print(sample_csv,sample_csv.shape)      (64197, 2)
# print(np.unique(y,return_counts=True))



y=y.values.reshape(-1,1)

ohe = OneHotEncoder(sparse=False)
ohe = OneHotEncoder()
y_ohe = ohe.fit_transform(y).toarray()

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


x_train,x_test,y_train,y_test=train_test_split(x,y_ohe,train_size=0.8,random_state=333,
                                               stratify=y_ohe
                                               )
from imblearn.over_sampling import SMOTE
smote= SMOTE(random_state=333)
x_train,y_train = smote.fit_resample(x_train,y_train)

scaler = RobustScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
test_csv = scaler.transform(test_csv)

#2.모델구성
model=Sequential()
model.add(Dense(7,input_shape=(13,),activation='relu'))
model.add(Dense(44,activation='relu'))
model.add(Dense(44,activation='relu'))
model.add(Dense(30,activation='relu'))
model.add(Dense(24,activation='relu'))
model.add(Dense(2,activation='relu'))
model.add(BatchNormalization())
model.add(Dense(48,activation='relu'))
model.add(Dense(7,activation='softmax'))

model.save("c:\_data\_save\대출모델61.h5")
#3.컴파일 훈련

from keras.callbacks import EarlyStopping,ModelCheckpoint
es= EarlyStopping(monitor='val_loss',mode='min',patience=1000,verbose=1,restore_best_weights=True)
mcp = ModelCheckpoint(
    monitor='val_loss',
    mode='auto',
    verbose=1,
    save_best_only=True,
    filepath='..\_data\_save\MCP\대출61.hdf5'
    )

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
hist= model.fit(x_train, y_train, epochs=100000,batch_size=5000, validation_split=0.2,verbose=3,
          callbacks=[es,mcp]
            )

model.save("c:\_data\_save\대출61.h5")

#4.결과예측
loss = model.evaluate(x_test, y_test)
y_submit = model.predict(test_csv)
y_test_indices = np.argmax(y_test, axis=1)
y_submit_indices = np.argmax(y_submit, axis=1)

y_submit = ohe.inverse_transform(y_submit)
y_submit = pd.DataFrame(y_submit)
sample_csv["대출등급"]=y_submit

sample_csv.to_csv(path + "대출61.csv", index=False)

y_pred= model.predict(x_test)
y_pred= ohe.inverse_transform(y_pred)
y_test = ohe.inverse_transform(y_test)
f1=f1_score(y_test,y_pred, average='macro')


print("f1",f1)
print("로스:", loss[0])
print("acc", loss[1])

'''
f1 0.891312217217633             
로스: 0.3271655738353729
acc 0.9065420627593994

f1 0.8712372872683251           1번   랜덤 8
로스: 0.3323124647140503
acc 0.8902388215065002

f1 0.8671034922838211         3번   랜덤 3
로스: 0.31909844279289246
acc 0.8996884822845459
r1 12
r2 11
r3 19
r4 35
r5 17
r6 40

f1 0.8834007722701109         4번
로스: 0.26390382647514343     random=3
acc 0.9125648736953735
r1 7
r2 44
r3 30
r4 24
r5 2
r6 48

f1 0.8894838905746612         5번
로스: 0.2839607000350952      random=4
acc 0.9067497253417969
r1 7                        c:\_data\_save\dechul_3
r2 44                         MCP 3번
r3 30
r4 24
r5 2
r6 48

f1 0.9154486155235781         7번
로스: 0.20493708550930023     MCP7
acc 0.928764283657074         dechul 7

f1 0.9143798222511382         8번
로스: 0.2211541086435318      MCP8
acc 0.9261682033538818        dechul 8

f1 0.908144693383551          9번
로스: 0.2306884527206421      MCP9
acc 0.9255451560020447      dechul 9
'''
