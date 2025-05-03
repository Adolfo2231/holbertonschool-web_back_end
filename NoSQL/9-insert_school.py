#!/usr/bin/env python3
"""
Module for inserting a document in a collection
"""
from typing import Dict, Any
from pymongo.collection import Collection
from pymongo.results import InsertOneResult


def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
        **kwargs: keyword arguments to be used as document fields
    Returns:
        The new _id
    """
    result: InsertOneResult = mongo_collection.insert_one(kwargs)
    return result.inserted_id
