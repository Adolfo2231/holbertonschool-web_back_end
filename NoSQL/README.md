# NoSQL - MongoDB

## Description
This project focuses on learning and implementing NoSQL database operations using MongoDB. It covers basic to advanced database operations including querying, inserting, updating, and deleting documents, as well as working with MongoDB from Python using PyMongo.

## Learning Objectives
- Understand what NoSQL means and the difference between SQL and NoSQL
- Comprehend ACID properties and document storage
- Learn about different NoSQL types and their benefits
- Perform database operations in MongoDB
- Utilize MongoDB with Python through PyMongo

## Requirements
- MongoDB 4.4
- Python 3.9
- PyMongo 4.x

## File Descriptions

### MongoDB Commands
- **0-list_databases**: Lists all databases in MongoDB
- **1-use_or_create_database**: Uses or creates the database `my_db`
- **2-insert**: Inserts a document with name="Holberton school" in the collection `school`
- **3-all**: Lists all documents in the collection `school`
- **4-match**: Lists all documents with name="Holberton school" in the collection `school`
- **5-count**: Displays the number of documents in the collection `school`
- **6-update**: Updates documents with name="Holberton school" to add address="972 Mission street"
- **7-delete**: Deletes all documents with name="Holberton school" from the collection `school`

### Python Scripts
- **8-all.py**: Function to list all documents in a collection
- **9-insert_school.py**: Function to insert a new document in a collection based on kwargs
- **10-update_topics.py**: Function to update school topics based on name
- **11-schools_by_topic.py**: Function to find schools with a specific topic
- **12-log_stats.py**: Script that provides stats about Nginx logs stored in MongoDB

## Usage
### MongoDB Commands
Run MongoDB commands with:
```bash
mongo < file_name
```

### Python Scripts
Run Python scripts with:
```bash
python3 script_name.py
```

## Author
Adolfo Rodriguez