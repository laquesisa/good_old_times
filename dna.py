import pandas as pd

names = ["Name", "Birthyear", "Language", "LocationLat", "LocationLong", "Gender"]
dataset = pd.read_csv("userData.csv")

#raw_data = pd.Categorical(dataset)
dataset.Gender = pd.Categorical(dataset.Gender)
dataset['GenderNum'] = dataset.Gender.cat.codes

dataset.Language = pd.Categorical(dataset.Language)
dataset['LanguageNum'] = dataset.Language.cat.codes

print(dataset)





