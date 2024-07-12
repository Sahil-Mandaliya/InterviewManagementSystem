import json
from typing import List
from pydantic import BaseModel, ValidationError
from django.core.exceptions import BadRequest

def convert_json_to_pydantic(json_data: dict, model_class: BaseModel):
    try:
        # Create an instance of the Pydantic model
        model_instance = model_class(**json_data)
        return model_instance
    except ValidationError as e:
        raise BadRequest(f"Validation error: {e}")
    except json.JSONDecodeError as e:
        raise BadRequest(f"JSON decode error: {e}")
    
def convert_json_list_to_pydantic_list(json_data_list: List[dict], model_class: BaseModel):
    new_list = []
    for json_data in json_data_list:
        try:
            # Create an instance of the Pydantic model
            model_instance = model_class(**json_data)
            new_list.append(model_instance)
        except ValidationError as e:
            raise BadRequest(f"Validation error: {e}")
        except json.JSONDecodeError as e:
            raise BadRequest(f"JSON decode error: {e}")

    return new_list



def pydantic_to_json(model_class: BaseModel):
    return model_class.dict(exclude_none=True)

def pydantic_list_to_json(model_class_list):
    new_list = []
    for item in model_class_list:
        new_list.append(item.dict(exclude_none=True))
    
    return new_list