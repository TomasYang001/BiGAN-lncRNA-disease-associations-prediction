import pandas as pd
import numpy as np

data_LDA = pd.read_csv('./processed data/similarity features/association matrix.csv',header = None)
data_L = pd.read_csv('./processed data/similarity features/Integrated similatiry of lncRNAs.csv',header = None)
data_D = pd.read_csv('./processed data/similarity features/Integrated similarity of diseases.csv',header = None)

Headers_423 = np.arange(423)+1
Headers_5714 = np.arange(5714)+1

data_LDA.columns , data_LDA.index = Headers_5714, Headers_423
data_L.columns, data_L.index = Headers_5714, Headers_5714
data_D.columns, data_D.index = Headers_423, Headers_423

print(data_LDA)
print(data_L)
print(data_D)

# labeled feature
data_label_feature = pd.DataFrame(columns = np.arange(6137)+1, index = np.arange(7696)+1)
# for storing positions of lncRNA and disease in feature set
# [j,i] j for disease , i for lncRNA
data_label_feature_position = pd.DataFrame(columns = np.arange(2)+1, index = np.arange(7696)+1)
count = 1
for i in range(1,5715):
    for j in range(1,424):
        if data_LDA[i][j] != 0:
            data_label_feature.loc[count] = (data_L[i].append(data_D[j])).to_numpy()
            data_label_feature_position.loc[count] = [j,i]
            count += 1

data_label_feature.to_csv('./feature result/data_label_feature.csv',header = None,index = None)
data_label_feature_position.to_csv('./feature result/data_label_feature_position.csv',header = None, index = None)

print(data_label_feature)

# unlabeled fearure
data_unlabel_feature = pd.DataFrame(columns = np.arange(6137)+1, index = np.arange(2282426)+1)
# for storing positions of lncRNA and disease in feature set
# [j,i] j for disease , i for lncRNA
data_unlabel_feature_position = pd.DataFrame(columns = np.arange(2)+1, index = np.arange(2282426)+1)
count = 1
for i in range(1,5415):
    for j in range(1,424):
        if data_LDA[i][j] == 0:
            data_unlabel_feature.loc[count] = (data_L[i].append(data_D[j])).to_numpy()
            data_unlabel_feature_position.loc[count] = [j,i]
            count += 1

data_unlabel_feature.to_csv('./feature result/data_unlabel_feature.csv',header = None,index = None)
data_unlabel_feature_position.to_csv('./feature result/data_unlabel_feature_position.csv',header = None, index= None)
print(data_unlabel_feature)
