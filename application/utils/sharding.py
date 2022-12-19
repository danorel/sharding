from pymongo import MongoClient
from pymongo.database import Database


def init_sharding(
    admin_db: Database,
    db_name: str
) -> None:
    admin_db.command('enableSharding', db_name)


def index_sharding(
    admin_db: Database,
    db_name: str,
    collection_name: str
) -> None:
    admin_db.command(
        {
            'shardCollection': f'{db_name}.{collection_name}',
            'key': {'Pclass': 'hashed'},
        }
    )


def get_sharding_info(
    client: MongoClient,
    db_name: str
) -> dict:
    info = {}
    for doc in client.list_databases():
        if doc['name'] == db_name:
            info = doc['shards']
            break
    return info
