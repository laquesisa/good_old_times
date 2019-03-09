import pandas as pd
import pygeohash as gh
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

def plot_hierarchical_clustering(dataset):
    plotable = dataset[['birthyear', 'lat', 'lng', 'gender_num', 'language_num']]
    linked = linkage(plotable, 'single')

    labelList = dataset.name.values

    plt.figure(figsize=(10, 7))  
    dendrogram(linked,  
                orientation='left',
                labels=labelList,
                distance_sort='descending',
                show_leaf_counts=True)
    plt.show()

def plot_agglomerative_cluster(dataset):
    plotable = dataset[['birthyear', 'lat', 'lng', 'gender_num', 'language_num']]
    cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
    return cluster.fit_predict(plotable)

def import_data(source):
    # import dataset
    dataset = pd.read_csv(source)

    # quantify our data
    dataset.gender = pd.Categorical(dataset.gender)
    dataset['gender_num'] = dataset.gender.cat.codes

    dataset.language = pd.Categorical(dataset.language)
    dataset['language_num'] = dataset.language.cat.codes

    #dataset['geohash'] = dataset.apply(lambda x: gh.encode(x.lat, x.lng, precision=5), axis=1)
    #dataset['id'] = dataset.index

    return dataset

# plot dataset
dataset = import_data("userData.csv")
clusters= plot_agglomerative_cluster(dataset)
dataset['category'] = clusters
print(dataset)

plot_hierarchical_clustering(dataset)