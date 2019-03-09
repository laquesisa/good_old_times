import pandas as pd
import pygeohash as gh
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

def plot_hierarchical_clustering(dataset, columns):
    plotable = dataset[columns]
    linked = linkage(plotable, 'single')

    labelList = dataset.name.values

    plt.figure(figsize=(10, 7))  
    dendrogram(linked,  
                orientation='left',
                labels=labelList,
                distance_sort='descending',
                show_leaf_counts=True)
    plt.show()

def plot_agglomerative_cluster(dataset, columns):
    mlData = dataset[columns]
    cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
    return cluster.fit_predict(mlData)

def import_data(source):
    # import dataset
    dataset = pd.read_csv(source)

    # quantify our data
    dataset.gender = pd.Categorical(dataset.gender)
    dataset['gender_num'] = dataset.gender.cat.codes

    dataset.language = pd.Categorical(dataset.language)
    dataset['language_num'] = dataset.language.cat.codes
    
    dataset['interests'] = dataset.apply(lambda x: x.interests.split(';'), axis=1)
    interests = pd.get_dummies(dataset['interests'].apply(pd.Series).stack()).sum(level=0)
    additional_columns = interests.columns.get_values().tolist()
    print(additional_columns)
    dataset = dataset.merge(interests, on=dataset.index)
    #print(dataset)
    #dataset['geohash'] = dataset.apply(lambda x: gh.encode(x.lat, x.lng, precision=5), axis=1)
    #dataset['id'] = dataset.index

    return dataset, additional_columns

# plot dataset
dataset, additional_columns = import_data("userData.csv")

columns = ['birthyear', 'lat', 'lng', 'gender_num', 'language_num'] + additional_columns

clusters= plot_agglomerative_cluster(dataset, columns)
dataset['category'] = clusters
#print(dataset[['name', 'category']] )

plot_hierarchical_clustering(dataset, columns)