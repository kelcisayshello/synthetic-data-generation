from faker import Faker

fake = Faker()

user_id = 1 

def generate_user_data() -> dict:
    """
    Generates a dictionary containing synthetic user information. This function relies on a global `user_id` variable to maintain unique user IDs.

    Returns:
        (dict): A dictionary representing a user with the following keys:
            - user_id (int): A unique identifier for each user record.
            - username (str): A unique username for the user.
            - password_hash (str): A placeholder for a securely hashed password (not implemented here).
            - email_address (str): A valid email address for the user.
            - created_at (str): A formatted date representing the user's account creation time.
            - first_name (str): The user's first name.
            - last_name (str): The user's last name.
            - date_of_birth (str): A formatted date representing the user's date of birth.
    """

    global user_id

    user_dictionary = {
        'user_id': user_id,
        'username': fake.user_name(),
        'password_hash': fake.password(),  # In a real application, you'd use a secure hashing algorithm
        'email_address': fake.email(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'created_at': fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
        'date_of_birth': fake.date_of_birth(minimum_age=13, maximum_age=130).strftime('%Y-%m-%d')
    }

    user_id += 1
    return user_dictionary