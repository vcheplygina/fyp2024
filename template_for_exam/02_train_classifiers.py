import pandas as pd
import numpy as np

# Default packages for the minimum example
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GroupKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
import pickle  # for saving/loading trained classifiers


# Where did we store the features?
file_features = "features/features.csv"
feature_names = ["asymmetry", "compactness", "mean_r", "mean_g", "mean_b"]

# Load the features
df = pd.read_csv(file_features)


# Make the dataset, you can select different classes (see task 0)
x = np.array(df[feature_names])
label = np.array(df["diagnosis"])

# Categorize as cancer or non-cancer
cancer_types = ["MEL", "SCC", "BCC"]  # Cancerous diagnoses
y = np.isin(label, cancer_types)  # True for cancer, False for non-cancer
patient_id = df["patient_id"]


# # Prepare cross-validation - images from the same patient must always stay together
num_folds = 5
group_kfold = GroupKFold(n_splits=num_folds)
group_kfold.get_n_splits(x, y, patient_id)


# # Different classifiers to test out
classifiers = [KNeighborsClassifier(1), KNeighborsClassifier(5), LogisticRegression()]
num_classifiers = len(classifiers)


# Initialize storage for metric results
acc_val = np.empty([num_folds, num_classifiers])
prec_val = np.empty([num_folds, num_classifiers])
rec_val = np.empty([num_folds, num_classifiers])
f1_val = np.empty([num_folds, num_classifiers])


for i, (train_index, val_index) in enumerate(group_kfold.split(x, y, patient_id)):

    x_train = x[train_index, :]
    y_train = y[train_index]
    x_val = x[val_index, :]
    y_val = y[val_index]

    for j, clf in enumerate(classifiers):

        # Train the classifier
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_val)

        # Compute the metrics
        acc_val[i, j] = accuracy_score(y_val, y_pred)
        prec_val[i, j] = precision_score(y_val, y_pred, zero_division=0)
        rec_val[i, j] = recall_score(y_val, y_pred, zero_division=0)
        f1_val[i, j] = f1_score(y_val, y_pred, zero_division=0)


for j, clf_name in enumerate(["1-NN", "5-NN", "Logistic Regression"]):
    average_acc = np.mean(acc_val[:, j])
    average_prec = np.mean(prec_val[:, j])
    average_rec = np.mean(rec_val[:, j])
    average_f1 = np.mean(f1_val[:, j])

    print(
        "Classifier {}: \n- Average Accuracy: {:.3f} \n- Average Precision: {:.3f} \n- Average Recall: {:.3f} \n- Average F1 Score: {:.3f}\n".format(
            clf_name, average_acc, average_prec, average_rec, average_f1
        )
    )

# Let's say you now decided to use the 5-NN
classifier = KNeighborsClassifier(n_neighbors=5)

# It will be tested on external data, so we can try to maximize the use of our available data by training on
# ALL of x and y
classifier = classifier.fit(x, y)

# This is the classifier you need to save using pickle, add this to your zip file submission
filename = "groupXY_classifier.sav"
pickle.dump(classifier, open(filename, "wb"))
