import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

author_id = 1 

from datetime import datetime, timedelta

def calculate_death_date(birth_date: str, age_at_death: int):
    """
    Calculates the death date given a birth date string and an age at death,
    ensuring the death date is not in the future.

    Args:
        birth_date (str): Faker-generated birth date in the format of 'YYYY-MM-DD'.
        age_at_death (int): Age at which the person became deceased.

    Returns:
        str: Death date in the format 'YYYY-MM-DD', or None if the age is invalid 
               or would result in a future death date.
    """

    try:
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        death_date = birth_date + timedelta(days=365 * age_at_death)
        
        today = datetime.now()  # Get today's date

        if death_date > today:
            return "DNE"

        return death_date.strftime('%Y-%m-%d')
    except ValueError:
        return None  # Handle invalid birth date format
    
def generate_author_data() -> dict:
    """
    Generates a dictionary containing synthetic author information. This function relies on a global `author_id` variable to maintain unique author IDs.

    Returns:
        (dict): A dictionary representing an author with the following keys:
            - author_id (int): A unique identifier for each author record.
            - author_name (str): The full name of the author.
            - biography (str): A brief biography of the author.
            - birth_date (str): A formatted date representing the author's date of birth.
            - death_date (str, optional): A formatted date representing the author's date of death (may be None).
    """

    global author_id

    author_dictionary = {
        'author_id': author_id,
        'author_name': fake.name(), 
        'biography': fake.paragraph(nb_sentences=3),
        'birth_date': fake.date_between_dates(date_start=datetime(year=1924, month=1, day=1), date_end=datetime(year=2004, month=12, day=31)).strftime('%Y-%m-%d')
    }

    # add death_date with a certain probability (e.g., 30%)
    if random.random() < 0.47:
        author_dictionary['death_date'] = calculate_death_date(author_dictionary['birth_date'], random.randint(12, 70))
    else:
        author_dictionary['death_date'] = "DNE"

    author_id += 1
    return author_dictionary