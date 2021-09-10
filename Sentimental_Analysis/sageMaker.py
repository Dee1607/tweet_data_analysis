import random
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import boto3
import io


s3 = boto3.resource('s3')
bucket = s3.Bucket('traindatab00865413')
train_data = ''
for obj in bucket.objects.all():
    body = obj.get()['Body'].read()
    train_data = pd.read_csv(io.BytesIO(body), header=0, delimiter=",", low_memory=False)
train = train_data

# creating instance of label encoder
labelencoder = LabelEncoder()
# Assigning numerical values and storing in another column
train['Current_Word'] = labelencoder.fit_transform(train['Current_Word'])
train['Next_Word'] = labelencoder.fit_transform(train['Next_Word'])

pca = PCA(2)
train = pca.fit_transform(train)
print("Printing Train Data After Applying Principle Component Analysis...")
print(train)

print(train)
for i in range(2, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=100, n_init=5)
    kmeans.fit(train)
    score = silhouette_score(train, kmeans.labels_, metric='euclidean')
    if score > 0.6:
        break;

# Y label
y_kmeans = kmeans.predict(train)
train = pd.DataFrame(train)
train['y_kmeans'] = pd.DataFrame(y_kmeans)

# Silhouette Score calculation
score = silhouette_score(train, kmeans.labels_, metric='euclidean')
print('Silhouette Score: %.3f' % score)

#Centroid cluster
cent = kmeans.cluster_centers_
print('Centroid of Cluster', cent)

#Plotting the cluster
train = pd.DataFrame(train)
train['y_kmeans'] = pd.DataFrame(y_kmeans)
no = train['y_kmeans'].nunique()

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(no)]

for i in range(0,no):
    plt.scatter(train[train['y_kmeans'] == i].iloc[:, 0], train[train['y_kmeans'] == i].iloc[:, 1], color=color[i])

plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.title('Cluster plot(Train data)')

plt.show()


#Testing Dataset

bucket = s3.Bucket('testdatab00865413')

test_data = ''
for obj in bucket.objects.all():
    body = obj.get()['Body'].read()
    test_data = pd.read_csv(io.BytesIO(body), header=0, delimiter=",", low_memory=False)

test = test_data

# creating instance of labelencoder
labelencoder = LabelEncoder()
# Assigning numerical values and storing in another column
test['Current_Word'] = labelencoder.fit_transform(test['Current_Word'])
test['Next_Word'] = labelencoder.fit_transform(test['Next_Word'])

pca = PCA(2)
test = pca.fit_transform(test)
print("Printing Test Data After Applying Principle Component Analysis...")
print(test)

#Predicting the cluster labels for test data
y_kmeans = kmeans.predict(test)

#Plotting the cluster
test = pd.DataFrame(test)
test['y_kmeans'] = pd.DataFrame(y_kmeans)
no = test['y_kmeans'].nunique()

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(no)]

for i in range(0, no):
    plt.scatter(test[test['y_kmeans'] == i].iloc[:, 0], test[test['y_kmeans'] == i].iloc[:, 1], color=color[i])

plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.title('Cluster plot(Test data)')

plt.show()
