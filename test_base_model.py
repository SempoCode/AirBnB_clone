#!/usr/bin/python3
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Print the instance
print(my_model)

# Save the instance (updates updated_at)
my_model.save()
print(my_model)

# Convert the instance to a dictionary and print it
my_model_json = my_model.to_dict()
print(my_model_json)

# Print the dictionary keys and values with types
print("JSON of my_model:")
for key in my_model_json.keys():
    pr = "\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key])
    print(pr)
