from pymongo import MongoClient
import pandas as pd
client = MongoClient('mongodb://goodoldtimes:HN88VIootmZYoM1feiOq0cqpReDHOJ3wdnF5EAbD02E0qNZrLVlSTSQXuMi9XPuNPX55cbK5E4ol4m8cbYIBXg==@goodoldtimes.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')
db = client['goodoldtimes']
users = db.users
df = pd.read_csv("userData.csv") #csv file which you want to import
records_ = df.to_dict(orient = 'records')
result = db.users.insert_many(records_ )