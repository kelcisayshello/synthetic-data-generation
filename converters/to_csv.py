import csv

def dict_to_csv(data: dict, filename: str):
  """
  Converts a dictionary to a CSV file, handling various data types gracefully.

  Args:
      data (dict): A dictionary where keys are column names and values are lists or single values.
      filename (str): The name of the CSV file to be created.
  """

  with open(filename, 'w', newline='') as csv_file:
    fieldnames = data.keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    max_rows = max(len(v) if isinstance(v, list) else 1 for v in data.values())

    for i in range(max_rows):
        row = {}
        for key, value in data.items():
            if isinstance(value, list):
                row[key] = value[i] if i < len(value) else ''
            else:
                row[key] = value if i == 0 else ''

        writer.writerow(row)
        
def list_of_dict_to_csv(data_list: list, filename: str):
  """
  Converts a dictionary to a CSV file, handling various data types gracefully.

  Args:
      data (list): A list of dictionaries where keys are column names and values are lists or single values.
      filename (str): The name of the CSV file to be created.
  """

  with open(filename, 'w', newline='') as csv_file:
    # Get fieldnames (column headers) from the first dictionary (assuming all have the same keys)
    fieldnames = data_list[0].keys() if data_list else []
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header

    for row_dict in data_list:  # Iterate over each dictionary in the list
        writer.writerow(row_dict)  # Write the dictionary as a row