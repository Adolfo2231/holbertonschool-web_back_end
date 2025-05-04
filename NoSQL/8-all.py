#!/usr/bin/env python3
"""
Module for listing all documents in a collection
"""
from typing import List, Dict, Any
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Lists all documents in a collection
    Args:
        mongo_collection: pymongo collection object
    Returns:
        List of all documents or empty list if no documents
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
