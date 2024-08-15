from faker import Faker
import random

fake = Faker()

saved_book_id = 1 
user_id = 1
unavailable_book_ids = set()

def skew_rating():
    """Generates a random decimal rating from 1 to 5, skewed towards 2 to 3.9."""

    rand_num = random.random()
    
    if rand_num < 0.8:  # 80% chance of getting a rating between 2 and 3.9
        return round(random.uniform(2, 3.9), 1)
    else:
        return round(random.uniform(1, 5), 1)

def generate_favoritebook_data(book_count) -> dict:
    """
    Generates a dictionary containing synthetic saved book information. 
    This function relies on global `saved_book_id` and `user_id` variables 
    to maintain unique IDs.

    Returns:
        (dict): A dictionary representing a saved book with the following keys:
            - saved_book_id (int): A unique identifier for each saved book record.
            - user_id (int): The unique identifier associated with the user who saved the book
            - book_id (int): The unique identifier of the book that was saved.
            - notes (str): Notes added by the user about the book
            - user_rating (float): A rating between 0 and 5 (inclusive) given by the user
            - read_status (str): The reading status of the book ('Not Started', 'In Progress', 'Completed')
    """

    global saved_book_id
    global user_id
    global unavailable_book_ids

    # continues to generate id's until a unique book_id is found
    while True:
        book_id = random.randint(1, book_count)
        if book_id not in unavailable_book_ids:
            unavailable_book_ids.add(book_id)
            break   

    saved_book_dictionary = {
        'saved_book_id': saved_book_id,
        'user_id': user_id,
        'book_id': book_id,
        'notes': fake.paragraph(),
        'user_rating': skew_rating(),
        'read_status': random.choices(['Not Started', 'In Progress', 'Completed'], weights=[0, 3, 7])[0]
    }

    saved_book_id += 1
    
    # increments user_id only occasionally to simulate multiple saved books per user
    if random.random() < 0.2:  # 20% chance of incrementing user_id
        user_id += 1

    return saved_book_dictionary