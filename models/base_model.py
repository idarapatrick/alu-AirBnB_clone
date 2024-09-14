#!/usr/bin/python3                                                                 
"""
BaseModel class for managing instance attributes
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initializes the instance with unique ID and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


    def save(self):
        """Updates the timestamp of the instance."""
        self.updated_at = datetime.utcnow()


    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()  # Removed extra space in "created_at "
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict


    def __str__(self):
        """Returns a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()  # Corrected method name to lowercase 'save'
    print(my_model)

    my_model_json = my_model.to_dict()
    print("JSON of my_model:")

    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))  # Fixed format for printing values
