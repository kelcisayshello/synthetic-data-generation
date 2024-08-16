from faker import Faker
import random

fake = Faker()

BOOK_AGE_CLASSIFICATIONS = [
    'Picture Books', 'Early Readers', 'Chapter Books', 'Teens', 'Young Adult (YA)', 'Adult'
]

BOOK_GENRES = [
    'Action and Adventure', 'Art', 'Biography', 'Business', 'Christian', 'Classics', 
    'Comics', 'Contemporary', 'Cookbooks', 'Crime', 'Fantasy', 'Feminist', 'Historical Fiction', 
    'History', 'Horror', 'Humor and Comedy', 'LGBTQ+', 'Manga', 'Memoir', 'Music', 'Mystery', 
    'Nonfiction', 'Paranormal', 'Philosophy', 'Poetry', 'Politics', 'Psychology', 'Religion', 
    'Romance', 'Satire', 'Science', 'Science Fiction', 'Self Help', 'Short Stories', 'Spirituality', 
    'Suspense and Thriller', 'Travel', 'True Crime', 'Western'
]

def generate_random_genres(genres: list[str]) -> str:
    """
    Randomly generates a comma-separated string of genres.

    Args:
        genres (list[str]): A list of available genres to choose from.

    Returns:
        (str): A comma-separated string containing a random selection of genres,
        with a maximum of 4 genres included.
    """

    num_genres = random.randint(1, 4) 
    selected_genres = random.sample(genres, num_genres)
    return ", ".join(selected_genres)

def skew_rating_count():
    """Generates a random count for reviews, biased towards numbers under 1,000,000."""
    
    reviews_count = [0, 1] 
    weights = [8, 1]     
    choice = random.choices(reviews_count, weights=weights)[0]
    
    if choice == 0:
        return random.randint(0, 2000000)
    else:
        return random.randint(2000000, 8000000)

def skew_rating():
    """Generates a random decimal rating from 1 to 5, skewed towards 2 to 3.9."""

    rand_num = random.random()
    
    if rand_num < 0.8:  # 80% chance of getting a rating between 2 and 3.9
        return round(random.uniform(2, 3.9), 1)
    else:
        return round(random.uniform(1, 5), 1)
    
book_id = 1

def generate_book_data() -> dict:
    """
    Generates a dictionary containing synthetic book information. This function relies on a global `book_id` variable to maintain unique book IDs.

    Returns:
        (dict): A dictionary representing a book with the following keys:
            - book_id (int): A unique identifier for each book record.
            - title (str): Title of the book.
            - isbn13 (str): A randomly generated 13-digit ISBN number.
            - publication_year (int): A random year between 1970 and 2024, with skewed distribution towards years after 1988.
            - genre (str): A comma-separated string of randomly selected genres.
            - age_classification (str): A randomly chosen age classification.
            - publisher (str): A randomly generated publisher name.
            - synopsis (str): A randomly generated book synopsis.
            - average_rating (float): Average rating with skewed distribution (float).
            - rating_count (int): Number of ratings given (integer).
            
        Keys coming soon include:
            - series (str): A randomly generated series title.
            - volume_number (int): Denoted volume, if exists.
            - edition (int): Denoted book edition, if exists.
    """

    global book_id

    book_dictionary = {
        'book_id': book_id,
        'title': fake.sentence(nb_words=4)[:-1], 
        'isbn13': fake.isbn13(),
        'publication_year': random.randint(1970, 2024),
        'genre': generate_random_genres(BOOK_GENRES),
        'age_classification': random.choice(BOOK_AGE_CLASSIFICATIONS),
        'publisher': fake.company(),
        'synopsis': fake.paragraph(nb_sentences=4),
        'average_rating': skew_rating(),
        'rating_count': skew_rating_count()
    }

    book_id += 1
    return book_dictionary