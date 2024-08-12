import os
import sys
from generators import *
from converters import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    while True:
        try:
            int_content_type = int(input("""Hello 👋🏾! Which media content would you like to generate? \n[1] Books \n[2] TV Shows\n[3] Movies\nEnter your choice: """))
            
            if 1 <= int_content_type <= 3:
                break  # exits the loop if the input is valid
            else:
                print("Sorry, that is an invalid choice. Please enter a number between [1] and [3].")
        except ValueError:
            print("ValueError: invalid input. That is not a number. Please try again.\n")
            # clear_screen()
            
    str_content_type = ""
    if int_content_type == 1:
        str_content_type = "books"
    elif int_content_type == 2:
        str_content_type = "TV shows"
    else:
        str_content_type = "movies"
        
    clear_screen()
    while True:
        try:
            CONTENT_COUNT = int(input("How many " + str_content_type + " do you want to generate?\nEnter a valid number less than nine quintillion: "))

            if 0 <= CONTENT_COUNT < 9223372036854775807:
                break 
            else:
                print("Sorry, that is an invalid choice. Please enter a positive number less than nine quintillion.\n")
        except ValueError:
            print("ValueError: invalid input. That is not a number. Please try again.\n")
    database = [] 
    
    for _ in range(CONTENT_COUNT):
        if int_content_type == 1:
            content_record = generate_book_data()
            database.append(content_record)
        elif int_content_type == 2:
            content_record = generate_show_data()
            database.append(content_record)
        else:
            print("Sorry, not ready yet!")
        
    clear_screen()
    extension = int(input("How would you like to export your " + str_content_type + " database?\n[1] Export to CSV\n[2] Export to JSON\nEnter your choice: "))
    print("Congrats 🎉! Your database is ready.")
    
    sample_path = './sample_outputs/' + str_content_type
    
    if extension == 1:
        list_of_dict_to_csv(database, sample_path + '.csv')
    else:
        list_of_dict_to_json(database, sample_path + '.json')
    
if __name__ == "__main__":
    main()