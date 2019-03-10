from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient
import pandas as pd
from dna import import_data_frame, plot_agglomerative_cluster
from bson.objectid import ObjectId
client = MongoClient('mongodb://goodoldtimes:HN88VIootmZYoM1feiOq0cqpReDHOJ3wdnF5EAbD02E0qNZrLVlSTSQXuMi9XPuNPX55cbK5E4ol4m8cbYIBXg==@goodoldtimes.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')
db = client['goodoldtimes']

usercollection = db['users']

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route('/users/<user_id>', methods = ['GET'])
def get_recommended_user(user_id):
    if request.method == 'GET':
        user = usercollection.find_one({"_id": ObjectId(user_id)})
        category = user['category']
        users = usercollection.find({"_id": {'$ne': ObjectId(user_id)}, "category": category})

        return jsonify(list(users))
        result = []
        for user in users:
            print(user)
            result.append(user['name'])
        return ', '.join(result)
    else:
        return "hello"
        # POST Error 405 Method Not Allowed

@app.route('/users', methods = ['POST'])
def create_user():
    if request.method == 'POST':
        json = request.get_json()
        # name = json["name"]
        # age = json["age"]
        # user = {
        #     'name': 'Alex'
        # }
        # user_id = usercollection.insert_one(user).inserted_id
        
        users = pd.DataFrame(list(usercollection.find()))
        # print(users)
        dataset, additional_columns = import_data_frame(users)
        columns = ['birthyear', 'lat', 'lng', 'gender_num', 'language_num'] + additional_columns
        clusters= plot_agglomerative_cluster(dataset, columns)
        dataset['category'] = clusters

        for index, row in dataset.iterrows():
            usercollection.update_one(
                {"_id": row['_id']},
                {"$set":
                {"category": row['category']
            }})

        #modify/update the information for <user_id>
        data = request.form
        # return user_id
        return "hello"
    else:
        return "hello"
        # POST Error 405 Method Not Allowed