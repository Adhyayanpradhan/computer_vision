#https://keras.io/layers/core/
from numpy import loadtxt
from keras.models import Sequential#or model=Sequential
from keras.layers import Dense#or keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)

#load dataset.If we open the datasets we can see 9 column.The fiest 8 are input
#and last one is output in(0 and 1) as this is a binary classification.

dataset=loadtxt("pima-indians-diabetes.csv.txt",delimiter=',')
#print(dataset)
x=dataset[:,0:8]
y=dataset[:,8]

#define keras model
model=Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

#compile the model
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

#train the network in keras
model.fit(x,y,epochs=150,batch_size=10)

#evaluate the model
_,accuracy=model.evaluate(x,y)
print('Accuracy:%.2f'%(accuracy*100))
