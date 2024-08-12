from faker import Faker
import random

fake = Faker()

TV_SHOW_GENRES = [
    'Action', 'Adventure', 'Animation', 'Anime', 'Biography', 'Comedy', 'Crime', 'Docuseries', 'Drama', 'Family', 'Feel Good', 'Religion', 'Fantasy', 'Game Show', 'History', 'Horror', 'Medical', 'Music', 'Mystery', 'News', 'Reality', 'Romance', 'Sci-Fi', 'Soap Opera', 'Sports', 'Talk Show', 'Thriller', 'War', 'Western', 'Podcast'
]

def generate_random_genres(genres: list[str]):
    """Generates a string of random genres, with a maximum of 3 genres per TV show."""

    num_genres = random.randint(1, 3)
    selected_genres = random.sample(genres, num_genres)
    return ", ".join(selected_genres)

def skew_rating():
    """Generates a random decimal rating from 1 to 5, skewed towards 2 to 3.9."""

    rand_num = random.random()
    
    if rand_num < 0.8:  # 80% chance of getting a rating between 2 and 3.9
        return round(random.uniform(2, 3.9), 1)
    else:
        return round(random.uniform(1, 5), 1)
    
def skew_review_count():
    """Generates a random count for reviews, biased towards numbers under 1,000,000."""
    reviews_count = [0, 1] 
    weights = [5, 1]     
    choice = random.choices(reviews_count, weights=weights)[0]
    
    if choice == 0:
        return random.randint(0, 400000)
    else:
        return random.randint(400000, 999999)
    
def skew_premiere_year():
    """Generates a random premiere year between 1888 and 2024, skewed towards shows after 1989."""

    rand_num = random.random()
    
    if rand_num < 0.95:  # 95% chance of getting a more modern show
        return random.randint(1989, 2024)
    else:
        return random.randint(1888, 1989)

show_id = 1

def generate_show_data():
    """Generates a dictionary containing synthetic TV show information."""

    global show_id

    show_data = {
        'show_id': show_id,
        'title': fake.sentence(nb_words=5)[:-1],
        'genre': generate_random_genres(TV_SHOW_GENRES),
        'premiere_year': skew_premiere_year(),
        'status': random.choices(['Ongoing', 'On Hiatus', 'Ended'], weights=[1, 0.1, 5])[0],
        'number_of_seasons': random.randint(1, 60),
        'number_of_episodes': random.choices([random.randint(2, 60), random.randint(61, 300)], weights=[5, 1])[0],
        'description': fake.paragraph(),
        'average_rating': skew_rating(),
        'number_of_ratings': skew_review_count()
    }

    show_id += 1
    return show_data