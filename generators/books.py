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

def generate_random_genres(genres: list[str]):
    """Generates a string of random genres, with a maximum of 4 genres per book."""

    num_genres = random.randint(1, 4)  # Choose between 1 and 4 genres
    selected_genres = random.sample(genres, num_genres)  # Randomly select genres without repetition
    # print(selected_genres)
    return ", ".join(selected_genres)  # Join genres into a comma-separated string

def skew_review_count():
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
def generate_book_data():
    """Generates a dictionary containing synthetic book information.""" 
    
    global book_id
    
    book_dictionary =  {
        'book_id': book_id,
        'title': fake.sentence(nb_words=4)[:-1], 
        'author': fake.name(),
        'isbn': fake.isbn13(),
        'publication_year': random.randint(1970, 2024),
        'genre': generate_random_genres(BOOK_GENRES),
        'age_classification': random.choice(BOOK_AGE_CLASSIFICATIONS),
        'publisher': fake.company(),
        'description': fake.paragraph(nb_sentences=3),
        'average_rating': skew_rating(),
        'number_of_ratings': skew_review_count()
    }
    
    book_id += 1
    return book_dictionary