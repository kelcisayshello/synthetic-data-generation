import os
import re
import sys
import config
import dialogue

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def value_error():
    print("ValueError: invalid input. That is not a number, please try again.\n")

def get_content_type():
    """
    Dynamically generates the menu options and prompts user to choose a content type.

    Returns:
        choice (int): The choice corresponding to the media type
    """

    while True:

        menu_options = "\n".join([f"[{key}] {value.title()}" for key, value in dialogue.CONTENT_TYPE_MAPPING.items()])
        
        try:
            choice = int(input(f"""What kind of synthetic content would you like to generate today?\n{menu_options}\nEnter the number corresponding to your choice: """))
            if choice in dialogue.CONTENT_TYPE_MAPPING:
                if dialogue.CONTENT_TYPE_MAPPING[choice] == "favorited books":
                    if config.USERS_COUNT >= 1 and config.BOOKS_COUNT >= 1:
                        return choice
                    else:
                        if config.USERS_COUNT == 0:
                            print(f"\n🚧 Looks like there isn't any USER data for that! Generate some USER data first.\n")
                            dialogue.main()
                        elif config.BOOKS_COUNT == 0: 
                            print(f"\n🚧 Looks like there isn't any BOOK data for that! Generate some BOOK data first.\n")
                            dialogue.main()
                else:
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
            count = int(input(f"How many {content_type} do you want to generate?\nEnter a positive number: "))
            if 0 <= count < sys.maxsize:
                if content_type == "favorited books":
                    if count <= config.BOOKS_COUNT:
                        return count
                    else:
                        print(f"\nSorry, you need to enter a number equal to or less than {config.BOOKS_COUNT}.\n")
                else:
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

    while True:
        try:
            generate_more = int(input("Do you want to generate more data?\n[1] Yes \n[2] No\nEnter your choice: "))
            if 1 <= generate_more <= 2:
                if generate_more == 2:
                    print("Okay, glad I could help ✨! ")
                    sys.exit()
                else:
                    dialogue.main()
            else:
                print("Sorry, that is an invalid choice. Please select either [1] or [2].\n")
        except ValueError:
            value_error()
            
def update_config_variable_count(content_type, new_value):
    """
    Updates the corresponding variable in config.py based on the content_type.

    Args:
        content_type (str): The type of content being generated (e.g., "books", "shows", "movies").
        new_value: The new value to assign to the corresponding variable in config.py.
    """

    variable_name = content_type.upper().replace(" ", "_") + "_COUNT"  # Convert content_type to variable name

    if not hasattr(config, variable_name):
        print(f"Error: Variable {variable_name} not found in config.py")
        return

    setattr(config, variable_name, new_value)

    with open('config.py', 'r+') as f:
        content = f.read()
        new_content = re.sub(rf'{variable_name} = \d+', f'{variable_name} = {new_value}', content)
        f.seek(0)
        f.write(new_content)
        f.truncate()