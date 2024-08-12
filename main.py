import os
from generators import *
from converters import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()

        while True:
            try:
                int_content_type = int(input("""Hello 👋🏾! Which media content would you like to generate?\n[1] Books \n[2] TV Shows\n[3] Movies\nEnter your choice: """))
                
                if 1 <= int_content_type <= 3:
                    break
                else:
                    print("Sorry, that is an invalid choice. Please enter a number between [1] and [3].")
            except ValueError:
                print("ValueError: invalid input. That is not a number. Please try again.\n")

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
                CONTENT_COUNT = int(input(f"How many {str_content_type} do you want to generate?\nEnter a valid number less than nine quintillion: "))

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
            elif int_content_type == 2:
                content_record = generate_show_data()
            else:
                content_record = generate_movie_data()
            database.append(content_record)

        clear_screen()
        while True:
            try:
                extension = int(input(f"How would you like to export your {str_content_type} database?\n[1] Export to CSV\n[2] Export to JSON\nEnter your choice: "))
                if 1 <= extension <= 2:
                    break
                else:
                    print("Sorry, that is an invalid choice. Please enter either [1] or [2].")
            except ValueError:
                print("ValueError: Invalid input. That is not a number. Please try again.\n")
        
        print("Congrats 🎉! Your database is ready.\n")

        if str_content_type == "TV shows":
            str_content_type = "tv_shows"
            
        sample_path = './sample_outputs/' + str_content_type

        if extension == 1:
            list_of_dict_to_csv(database, sample_path + '.csv')
        else:
            list_of_dict_to_json(database, sample_path + '.json')

        generate_more = int(input("Do you want to generate more data?\n[1] Yes \n[2] No\nEnter your choice: "))
        if generate_more != 1:
            break  # Exit the outer loop if the user doesn't want to continue
        print("Okay, glad I could help ✨! ")

if __name__ == "__main__":
    main()