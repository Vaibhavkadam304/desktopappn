from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from environs import Env

env = Env()
env.read_env()

app = Flask(__name__)
CORS(app)

DATABASE_URL = env.str('DATABASE_URL')
PORT = env.int('PORT', default=5000)

client = MongoClient(DATABASE_URL)
db = client['mydatabase']
collection = db['mycollection']

@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
