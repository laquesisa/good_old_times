from flask import Flask
from flask import request
from pymongo import MongoClient
import pandas as pd
from dna import import_data_frame, plot_agglomerative_cluster
client = MongoClient('mongodb://goodoldtimes:HN88VIootmZYoM1feiOq0cqpReDHOJ3wdnF5EAbD02E0qNZrLVlSTSQXuMi9XPuNPX55cbK5E4ol4m8cbYIBXg==@goodoldtimes.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')
db = client['goodoldtimes']

usercollection = db['users']

app = Flask(__name__)

@app.route('/users/<user_id>', methods = ['GET'])
def get_recommended_user(user_id):
    if request.method == 'GET':
        users = pd.DataFrame(list(usercollection.find()))

        dataset, additional_columns = import_data_frame(users)
        columns = ['birthyear', 'lat', 'lng', 'gender_num', 'language_num'] + additional_columns
        clusters= plot_agglomerative_cluster(dataset, columns)
        dataset['category'] = clusters

        print(dataset)

        result = []
        for user in usercollection.find():
            result.append(user['name'])
        return ', '.join(result)
    else:
        return "hello"
        # POST Error 405 Method Not Allowed

@app.route('/users', methods = ['POST'])
def create_user():
    if request.method == 'POST':
        user = {
            'name': 'Alex'
        }
        user_id = usercollection.insert_one(user).inserted_id
        #modify/update the information for <user_id>
        data = request.form
        # return user_id
        return "hello"
    else:
        return "hello"
        # POST Error 405 Method Not Allowed