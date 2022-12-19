import csv

from pymongo.database import Collection


def load_data(
    dataset_collection: Collection,
    dataset_path: str
) -> None:
    with open(dataset_path) as file:
        reader = csv.DictReader(file)
        dataset_collection.insert_many(
            [
                row for row in reader
            ]
        )
