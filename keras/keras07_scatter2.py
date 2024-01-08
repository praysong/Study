from keras.models import Sequential
from keras.layers import Dense
import numpy as np
#1. 데이터

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y=np.array([1,2,4,3,5,7,9,3,8,12,13,8,  14,15,9, 6,17,23,21,20])

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =train_test_split(x,y, test_size=0.3,random_state=1)

print(x_train)
print(y_train)
print(x_test)
print(y_test)

#2.모델구성
model=Sequential()
model.add(Dense(30,input_dim=1))
model.add(Dense(50))
model.add(Dense(90))
model.add(Dense(70))
model.add(Dense(50))
model.add(Dense(1))

#3.컴파일, 훈련
model.compile(loss='mse',optimizer='adam')
model.fit(x_train,y_train,epochs=1, batch_size=1)

#4.결과 예측
loss=model.evaluate(x_test,y_test)
result=model.predict([x])
print("로스 :",loss)
print("x 예측값",result)

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.plot(x, result,color='red')
plt.scatter(x, result,color='blue')
plt.show()


