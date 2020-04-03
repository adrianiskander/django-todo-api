import json


def getPublicFields(model):
    """
        Get model fields that will be send to public client.
    """
    return {
        'id': model.id,
        'title': model.title,
        'isDone': model.is_done
    }


def deserialize(json_data):
    data = json.loads(json_data)
    return {
        'id': data['id'],
        'title': data['title'],
        'is_done': data['isDone']
    }


def serialize(model):
    """
        Serialize single todo item model to json.
    """
    return json.dumps(getPublicFields(model))


def serialize_many(models_list):
    """
        Serialize list of todo item models to json.
    """
    data = {'todoItems': []}

    for model in models_list:
        data['todoItems'].append(getPublicFields(model))

    return json.dumps(data)
