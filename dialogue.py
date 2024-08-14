import os
import sys
import re
from generators import *
from converters import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def value_error():
    print("ValueError: invalid input. That is not a number, please try again.\n")
    
CONTENT_TYPE_MAPPING = {
    1: "books",
    2: "shows",
    3: "movies"
}

GENERATOR_FUNCTIONS = {
    1: generate_book_data,
    2: generate_show_data,
    3: generate_movie_data
}

def get_content_type():
    """
    Prompts the user to choose a content type, dynamically generating the menu from CONTENT_TYPE_MAPPING.

    Returns:
        choice (int): The choice corresponding to the media type
    """

    while True:
        # Dynamically generate the menu options
        menu_options = "\n".join([f"[{key}] {value.title()}" for key, value in CONTENT_TYPE_MAPPING.items()])
        
        try:
            choice = int(input(f"""What kind of synthetic content would you like to generate today?\n{menu_options}\nEnter the number corresponding to your choice: """))
            if choice in CONTENT_TYPE_MAPPING:
                return choice
            else:
                print("Sorry, that was an invalid choice. Please enter a valid number from the menu.")
        except ValueError:
            value_error()
            
def get_content_count(content_type: str):
    """Prompts user to input the number of content items to generate.
    
    Args:
        content_type (str): Indicates the user-chosen content type.
    
    Returns:
        count (int): Returns the count for the user's desired amount of content records to be generated.
    """

    clear_screen()
    while True:
        try:
            count = int(input(f"How many {content_type} do you want to generate?\nEnter a valid number less than nine quintillion: "))
            if 0 <= count < sys.maxsize:
                return count
            else:
                print("Sorry, that is an invalid choice. Please enter a positive number less than nine quintillion.\n")
        except ValueError:
            value_error()
            
def get_export_choice():
    """Prompts user to choose an export format."""

    clear_screen()
    while True:
        try:
            choice = int(input(f"And how would you like to export your synthetic data?\n[1] Export to CSV\n[2] Export to JSON\nEnter your choice: "))
            if 1 <= choice <= 2:
                return choice
            else:
                print("Sorry, that is an invalid choice. Please enter either [1] or [2].")
        except ValueError:
            value_error()
            
def get_output_file_path(extension: int):
    """Generates the output file path based on content type, extension, and user-provided filename.

    Args:
        extension (int): Integer relating to the user's choice of data export.

    Returns:
        (str): A string indicating details about the export type, content type, and the specified file path location.
    """

    file_extension = "csv" if extension == 1 else "json"

    while True:
        filename = input(f"Enter the desired filename (without extension): ")
        if filename and not re.search(r'[\\/:\*\?"<>|\s]', filename):  # Check if the filename is not empty
            break
        else:
            print("Please enter a valid filename. Avoid using spaces and these characters: \\ / : * ? \" < > |")

    return f'./sample_outputs/{filename}.{file_extension}'

def generate_more():
    """Prompts the user on whether they would like to continue generating more content."""

    clear_screen()
    while True:
        try:
            generate_more = int(input("Do you want to generate more data?\n[1] Yes \n[2] No\nEnter your choice: "))
            if 1 <= generate_more <= 2:
                if generate_more == 2:
                    print("Okay, glad I could help ✨! ")
                    sys.exit()
                else:
                    main()
            else:
                print("Sorry, that is an invalid choice. Please select either [1] or [2].\n")
        except ValueError:
            value_error()

def main():
    while True:
        user_content_choice = get_content_type()
        content_type = CONTENT_TYPE_MAPPING[user_content_choice]
        clear_screen()
        content_count = get_content_count(content_type)
        
        database = []
        generator_function = GENERATOR_FUNCTIONS[user_content_choice]
        for _ in range(content_count):
            content_record = generator_function()
            database.append(content_record)
            
        clear_screen()
        export_choice = get_export_choice()
        file_path = get_output_file_path(export_choice)
        
        if export_choice == 1:
            list_of_dict_to_csv(database, file_path)
        else:
            list_of_dict_to_json(database, file_path)
            
        print("Congrats 🎉! Your database is ready.")
        generate_more()
        
if __name__ == "__main__":
    clear_screen()
    print("🌟 Welcome to the Synthetic Data Generation tool! 🌟\n")
    main()