from generators import *
from converters import *

if __name__ == "__main__":
    
    # (1) Create a list to store synthetic book records
    synthetic_data = []
    
    # (2) Variable which denotes the amount of synthetic book records generated
    BOOK_COUNT = 200
    
    # (3) Function generates books based on requested count amount 
    for _ in range(BOOK_COUNT):
        book_record = generate_book_data()
        synthetic_data.append(book_record)

    # (4) Export data into formatted files
    list_of_dict_to_csv(synthetic_data, './sample_outputs/books.csv')
    list_of_dict_to_json(synthetic_data, './sample_outputs/books.json')