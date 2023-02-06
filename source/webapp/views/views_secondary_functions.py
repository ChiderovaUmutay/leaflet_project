serializer_data = {}


def get_serializer_data(obj, related_object, related_object_field=None):
    serializer_data["id"] = obj.id
    serializer_data["name"] = obj.name
    serializer_data["coordinates"] = obj.coordinates
    if related_object_field:
        serializer_data[related_object_field] = related_object
    return serializer_data
