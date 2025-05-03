#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection


def log_stats() -> None:
    """
    Provides stats about Nginx logs stored in MongoDB
    """
    client: MongoClient = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection: Collection = client.logs.nginx

    # Total logs
    total_logs: int = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods
    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count: int = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check
    status_check_count: int = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
