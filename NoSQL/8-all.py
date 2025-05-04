#!/usr/bin/env python3
"""
Module providing a function to list all documents in a MongoDB collection.
"""
from typing import List, Dict, Any
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List containing all documents in the collection,
        or empty list if no documents
    """
    if mongo_collection is None:
        return []
    documents = mongo_collection.find()
    return list(documents)


if __name__ == "__main__":
    pass
