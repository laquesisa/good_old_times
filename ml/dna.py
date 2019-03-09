import pandas as pd
import pygeohash as gh
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# import dataset
dataset = pd.read_csv("userData.csv")

# quantify our data
dataset.gender = pd.Categorical(dataset.gender)
dataset['gender_num'] = dataset.gender.cat.codes

dataset.language = pd.Categorical(dataset.language)
dataset['language_num'] = dataset.language.cat.codes

#dataset['geohash'] = dataset.apply(lambda x: gh.encode(x.lat, x.lng, precision=5), axis=1)
#dataset['id'] = dataset.index

# plot dataset
plotable = dataset.iloc[:, [1, 3, 4, 6, 7]]
print(plotable)
linked = linkage(plotable, 'single')

labelList = dataset.name.values

plt.figure(figsize=(10, 7))  
dendrogram(linked,  
            orientation='left',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()