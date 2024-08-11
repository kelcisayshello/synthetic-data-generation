import json

def list_of_dict_to_json(data_list: list, filename: str):
    """
    Converts a list of dictionaries to a JSON file.

    Args:
        data_list (list): A list of dictionaries, each representing an object.
        filename (str): The name of the JSON file to be created.
    """

    with open(filename, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)  # Write the list of dictionaries to the JSON file