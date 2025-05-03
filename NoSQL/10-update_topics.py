#!/usr/bin/env python3
"""
Module for updating topics of a school document
"""
from typing import List
from pymongo.collection import Collection
from pymongo.results import UpdateResult


def update_topics(
    mongo_collection: Collection, name: str, topics: List[str]
) -> None:
    """
    Changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name: string - the school name to update
        topics: list of strings - list of topics approached in the school
    """
    result: UpdateResult = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
