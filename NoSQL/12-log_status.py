#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """Function that provides stats about Nginx logs in MongoDB"""
    # Connect to the database
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_collection = db.nginx

    # Count the number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Display the number of documents per HTTP method
    methods = ["GET", "POST", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count GET methods and path=/status
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
