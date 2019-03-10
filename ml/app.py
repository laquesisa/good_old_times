from flask import Flask
from flask import request
from bson.json_util import dumps
from pymongo import MongoClient
import pandas as pd
from dna import import_data_frame, plot_agglomerative_cluster
from bson.objectid import ObjectId
from jsonschema import validate, ValidationError
from flask import Response

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

        return dumps(list(users))
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
        schema = {
            "type" : "object",
            "properties" : {
                "name" : {"type" : "string"},
                "birthyear" : {"type" : "string"},
                "language" : {"enum" : ["German", "French"]},
                "lat" : {"type" : "string"},
                "lng" : {"type" : "string"},
                "gender" : {"enum" : ["m", "f"]},
                "interests" : {"type" : "string"},
            },
            "required": ["name", "birthyear", "language", "lat", "lng", "gender", "interests"]
        }

        # if not JsonInputs(request).validate():
        #     print(errors)
        #     return "Please validate data"
        json = request.json
        try:
            validate(instance=json, schema=schema)
        except ValidationError as error:
            return Response(dumps({'error':error.message}), status=400,  mimetype='application/json')
            return str(error.message)
        user_id = usercollection.insert_one(json).inserted_id
        
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
        return str(user_id)
    else:
        return "hello"
        # POST Error 405 Method Not Allowed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)