
import os
import pandas as pd
import numpy as np

# Default packages for the minimum example
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GroupKFold
from sklearn.metrics import accuracy_score #example for measuring performance


import pickle #for saving/loading trained classifiers


#Where are the files
file_data = '..' + os.sep + 'data' + os.sep +'metadata.csv'
df = pd.read_csv(file_data)
label = np.array(df['diagnostic'])


#Where did we store the features?
file_features = 'features/features.csv'
feature_names = ['red','green','blue']

# Load the features - remember the example features are not informative
df_features = pd.read_csv(file_features)


# Make the dataset, you can select different classes (see task 0)
x = np.array(df_features[feature_names])
y =  label == 'NEV'   #now True means healthy nevus, False means something else
patient_id = df['patient_id']


#Prepare cross-validation - images from the same patient must always stay together
num_folds = 5
group_kfold = GroupKFold(n_splits=num_folds)
group_kfold.get_n_splits(x, y, patient_id)


#Different classifiers to test out
classifiers = [
    KNeighborsClassifier(1),
    KNeighborsClassifier(5)
]
num_classifiers = len(classifiers)

      
acc_val = np.empty([num_folds,num_classifiers])

for i, (train_index, val_index) in enumerate(group_kfold.split(x, y, patient_id)):
    
    x_train = x[train_index,:]
    y_train = y[train_index]
    x_val = x[val_index,:]
    y_val = y[val_index]
    
    
    for j, clf in enumerate(classifiers): 
        
        #Train the classifier
        clf.fit(x_train,y_train)
    
        #Evaluate your metric of choice (accuracy is probably not the best choice)
        acc_val[i,j] = accuracy_score(y_val, clf.predict(x_val))
   
    
#Average over all folds
average_acc = np.mean(acc_val,axis=0) 
   
print('Classifier 1 average accuracy={:.3f} '.format(average_acc[0]))
print('Classifier 2 average accuracy={:.3f} '.format(average_acc[1]))



#Let's say you now decided to use the 5-NN 
classifier = KNeighborsClassifier(n_neighbors = 5)

#It will be tested on external data, so we can try to maximize the use of our available data by training on 
#ALL of x and y
classifier = classifier.fit(x,y)

#This is the classifier you need to save using pickle, add this to your zip file submission
filename = 'groupXY_classifier.sav'
pickle.dump(classifier, open(filename, 'wb'))



