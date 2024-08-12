from faker import Faker
import random

fake = Faker()

MOVIE_LANGUAGES = ['English', 'Spanish', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi', 'German', 'Chinese', 'Korean', 'French', 'Tamil', 'Urdu', 'Turkish', 'Italian', 'Vietnamese', 'Thai', 'Polish', 'Ukrainian', 'Malayalam', 'Swahili', 'Amharic', 'Yoruba', 'Afrikaans', 'Dutch']

MOVIE_GENRES = [
    'Action', 'Adventure', 'Animation', 'Anime', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Religion', 'History', 'Horror', 'Medical', 'Music', 'Mystery', 'News', 'Reality', 'Romance', 'Sci-Fi', 'Soap Opera', 'Sports', 'International', 'Thriller', 'War', 'Western', 'Suspense',
]

def generate_random_genres(genres: list[str]):
    """Generates a string of random genres, with a maximum of 3 genres per TV show."""

    num_genres = random.randint(1, 3)
    selected_genres = random.sample(genres, num_genres)
    return ", ".join(selected_genres)

def skew_review_count():
    """Generates a random count for reviews, biased towards numbers under 1,000,000."""
    reviews_count = [0, 1] 
    weights = [8, 1]     
    choice = random.choices(reviews_count, weights=weights)[0]
    
    if choice == 0:
        return random.randint(0, 400000)
    else:
        return random.randint(400000, 999999)
    
def skew_rating():
    """Generates a random decimal rating from 1 to 5, skewed towards 2 to 3.9."""

    rand_num = random.random()
    
    if rand_num < 0.8:  # 80% chance of getting a rating between 2 and 3.9
        return round(random.uniform(2, 3.9), 1)
    else:
        return round(random.uniform(1, 5), 1)
    
def skew_premiere_year():
    """Generates a random premiere year between 1888 and 2024, skewed towards shows after 1989."""

    rand_num = random.random()
    
    if rand_num < 0.95:  # 95% chance of getting a more modern show
        return random.randint(1989, 2024)
    else:
        return random.randint(1888, 1989)

movie_id = 1

def generate_movie_data():
    """Generates a dictionary containing synthetic movie information."""

    global movie_id

    movie_dictionary = {
        'movie_id': movie_id,
        'title': fake.sentence(nb_words=5)[:-1], 
        'director': fake.name(),
        'release_year': skew_premiere_year(),
        'genre': generate_random_genres(MOVIE_GENRES),
        'duration_in_minutes': random.randint(40, 210),
        'description': fake.paragraph(nb_sentences=4),
        'average_rating': skew_rating(),
        'number_of_ratings': skew_review_count(),
        'language': random.choice(MOVIE_LANGUAGES),  # Assuming you have a MOVIE_LANGUAGES list
        'country_of_origin': fake.country(),
        'cast_members': [fake.name() for _ in range(random.randint(1, 15))], 
        'production_company': fake.company(),
        # 'tags': generate_random_genres(MOVIE_TAGS),  # Assuming you have a MOVIE_TAGS list
    }

    movie_id += 1
    return movie_dictionary