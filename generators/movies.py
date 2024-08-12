from faker import Faker
import random

fake = Faker()

MOVIE_GENRES = [
    'Action', 'Adventure', 'Animation', 'Anime', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Religion', 'History', 'Horror', 'Medical', 'Music', 'Mystery', 'News', 'Reality', 'Romance', 'Sci-Fi', 'Soap Opera', 'Sports', 'International', 'Thriller', 'War', 'Western', 'Suspense',
]

def generate_random_genres(genres: list[str]):
    """Generates a string of random genres, with a maximum of 3 genres per TV show."""

    num_genres = random.randint(1, 3)
    selected_genres = random.sample(genres, num_genres)
    return ", ".join(selected_genres)