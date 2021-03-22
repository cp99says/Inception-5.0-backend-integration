from flask import Flask
import pymongo

app=Flask(__name__)

CONNECTION_STRING='add your own connection string'
client=pymongo.MongoClient(CONNECTION_STRING)
db=client.get_database('sentifeed')
user_collection=pymongo.collection.Collection(db, 'sentimentAnalysis')
