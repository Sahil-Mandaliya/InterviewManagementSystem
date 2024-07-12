from pydantic import BaseModel
from django.core import serializers
from main.utils.pydantic import convert_json_to_pydantic, convert_json_list_to_pydantic_list
import json

def model_to_json(instance):
    """
    Convert a Django model instance to a JSON string.
    """
    serialized_obj = serializers.serialize('json', [instance])
    obj = json.loads(serialized_obj)[0]
    json_object = obj['fields']
    json_object['id'] = obj['pk'] 
    json_object.pop('created_at', None)
    json_object.pop('updated_at', None)
    return json_object

def model_list_to_json(instances):
    """
    Convert a list of Django model instances to a JSON string.
    """
    serialized_objs = serializers.serialize('json', instances)
    # Load the serialized JSON data
    serialized_data = json.loads(serialized_objs)
    
    # Extract the primary key and fields
    json_objects = []
    for obj in serialized_data:
        json_object = obj['fields']
        json_object['id'] = obj['pk']  # Include the primary key in the JSON object
        json_object.pop('created_at', None)
        json_object.pop('updated_at', None)

        json_objects.append(json_object)
    
    return json_objects

def db_model_to_pydantic(instance, pydantic_model_class: BaseModel):
    json_data = model_to_json(instance)
    return convert_json_to_pydantic(json_data, pydantic_model_class)

def db_model_list_to_pydantic(instances, pydantic_model_class: BaseModel):
    json_data = model_list_to_json(instances)
    return convert_json_list_to_pydantic_list(json_data, pydantic_model_class)