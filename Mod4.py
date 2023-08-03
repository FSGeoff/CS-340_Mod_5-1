from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #

        USER = "aacuser"
        PASS = "SNHU_Geoff_Nix"
        HOST = "nv-desktop-services.apporto.com"
        PORT = 30632
        DB = "AAC"
        COL = "animals"
        #
        # Initialize Connection
        #
        self.client = MongoClient("mongodb://%s:%s@%s:%d" % (USER, PASS, HOST, PORT))
        self.database = self.client["%s" % (DB)]
        self.collection = self.database["%s" % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            if isinstance(data, dict):
                result = self.database.animals.insert_one(data)  # data should be dictionary
                id = result.inserted_id
                return id
            else:
                raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria:
            data = self.database.animals.find(criteria, {"_id": False})
        else:
            data = self.database.animals.find({}, {"_id": False})

        return list(data)  # Convert the cursor to a list and return

    # Create method to implement the U in CRUD.
    def update(self, data, updated):
        if data is not None and updated is not None:
            if isinstance(data, dict) and isinstance(updated, dict):
                self.database.animals.update_one(data, {"$set": updated})
                return self.database.animals.find_one(data)
            else:
                raise Exception(
                    "Nothing to update, because query or update_data parameter is empty"
                )

    # Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            if isinstance(data, dict):
                result = self.database.animals.delete_one(data)
                return result.deleted_count
            else:
                raise Exception("Nothing to delete, because query parameter is empty")

    # Check to make sure the document exists
    def check(self, data):
        return self.database.animals.find_one(data)