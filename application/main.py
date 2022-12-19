import logging

from flask import Flask
from pymongo import MongoClient

from config import DATA_PATH, MONGO_URI, MONGO_DB, MONGO_COLLECTION
from utils.sharding import init_sharding, index_sharding, get_sharding_info
from utils.data import load_data

logging.basicConfig(filename='history.log', level=logging.DEBUG)
app = Flask(__name__)

client = MongoClient(MONGO_URI)


@app.route("/sharding/load")
def sharding_load():
    collection_db = client[MONGO_DB]
    collection_data = collection_db[MONGO_COLLECTION]
    load_data(collection_data, DATA_PATH)
    return f"Loaded data successfully!"


@app.route("/sharding/info")
def sharding_info():
    info = get_sharding_info(client, MONGO_DB)
    if len(info) == 0:
        return f"Shards: not enabled!"
    shard_0_size = info.get('shard0', 0)
    shard_1_size = info.get('shard1', 0)
    return f"Shards: [shard0={shard_0_size}, shard1={shard_1_size}]"


@app.route("/sharding/enable")
def enable_sharding():
    admin_db = client['admin']
    init_sharding(
        admin_db,
        MONGO_DB
    )
    index_sharding(
        admin_db,
        MONGO_DB,
        MONGO_COLLECTION
    )
    return "Server has enabled sharding for MongoDB database!"


@app.route("/")
def index():
    return "Server is running on localhost:8080!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
