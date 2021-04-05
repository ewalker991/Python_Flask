from flask import Flask, request, jsonify
# from peewee import *
# from playhouse.shortcuts import model_to_dict, dict_to_model

# db = PostgresqlDatabase('people', user='postgres', password='', host='localhost', port=5423)

# class BaseModel(Model):
#     class Meta:
#         database = db

# class Person(BaseModel):
#     name = CharField()
#     age = IntegerField()

# db.connect()
# db.drop_tables([Person])
# db.create_tables([Person])

app = Flask(__name__)

@app.route('/endpoint', methods = ['GET', 'PUT', 'POST', 'DELETE'])

def endpoint():
    if request.method == 'GET':
        return 'GET REQUEST'
    if request.method == 'PUT':
        return 'PUT REQUEST'
    if request.method == 'POST':
        return 'POST REQUEST'
    if request.method == 'DELETE':
        return 'DELETE REQUEST'
    # return "Hello, world!"

app.run(port = 9000, debug = True)