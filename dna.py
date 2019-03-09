import pandas as pd
import pygeohash as gh

# import dataset
dataset = pd.read_csv("userData.csv")

# quantify our data
dataset.gender = pd.Categorical(dataset.gender)
dataset['gender_num'] = dataset.gender.cat.codes

dataset.language = pd.Categorical(dataset.language)
dataset['language_num'] = dataset.language.cat.codes

dataset['geohash'] = dataset.apply(lambda x: gh.encode(x.lat, x.lng, precision=5), axis=1)

print(dataset)





