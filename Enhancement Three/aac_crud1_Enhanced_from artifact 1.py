import hashlib
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCRUD(object):
    """ CRUD operations for Animal collection in MongoDB with authentication """
    
    def __init__(self, host='localhost', port=27017, database='AAC', collection='animals', username=None, password=None):
        HOST = host
        PORT = port
        DB = database
        COL = collection
      
        if username and password:
            self.client = MongoClient(host=HOST, port=PORT, username=username, password=password, serverSelectionTimeoutMS=5000)
        else:
            self.client = MongoClient(host=HOST, port=PORT, serverSelectionTimeoutMS=5000)
            
        self.database = self.client[DB]
        self.collection = self.database[COL]
        self.users_collection = self.database['users']  # Collection for stored user accounts
        self.is_authenticated = False

    """ Function to check login details before letting someone use the database"""
    def login_user(self, username, password):
        user_record = self.users_collection.find_one({'username': username})
        
        if user_record and user_record.get('password') == password:
            self.is_authenticated = True
            print("Access allowed successfully.")
            return True
        else:
            print("Error: Wrong username or password entered.")
            self.is_authenticated = False
            return False

    """Function to check user input before sending it to MongoDB"""
    def check_input_data(self, input_data):
        # Check if inputData is empty or not a dictionary (bad format)
        if not input_data or not isinstance(input_data, dict):
            print("Error: Invalid data entered")
            return False
        else:
            # sendToDatabase equivalent (calls your create method)
            success = self.create(input_data)
            return success

    def create(self, data):
        """ Insert document into MongoDB """
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False
    
    def read(self, query):
        """ Query documents from MongoDB """
        try:
            cursor = self.collection.find(query)
            return list(cursor)  # convert cursor to list of documents
        except Exception as e:
            print(f"Error querying documents: {e}")
            return []
          
          
    def update(self, query, new_data):
        """ Update document in MongoDB"""
        try:
            result = self.collection.update_many(query, {'$set': new_data})
            return result.modified_count
        except Exception as e:
            print(f"An error occured: {e}")
            return 0              
      
            
    def delete(self, query):
        """ Delete a document in MongoDB"""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error occured: {e}")
            return 0
        