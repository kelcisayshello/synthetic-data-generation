from generators import *
from converters import *
import functions
import config

CONTENT_TYPE_MAPPING = {
    1: "books",
    2: "users",
    3: "favorite books",
    4: "authors",
}

GENERATOR_FUNCTIONS = {
    1: generate_book_data,
    2: generate_user_data,
    3: generate_favoritebook_data,
    4: generate_author_data
}

def main():
    while True:
        user_content_choice = functions.get_content_type()
        content_type = CONTENT_TYPE_MAPPING[user_content_choice]
        
        functions.clear_screen()
            
        content_count = functions.get_content_count(content_type)
        
        functions.update_config_variable_count(content_type, content_count)
        database = []
        generator_function = GENERATOR_FUNCTIONS[user_content_choice]
            
        for _ in range(content_count):
            
            if generator_function == generate_favoritebook_data:
                content_record = generator_function(config.BOOKS_COUNT)
            else:
                content_record = generator_function()
            database.append(content_record)
            
        functions.clear_screen()
        
        export_choice = functions.get_export_choice()
        file_path = functions.get_output_file_path(export_choice)
        
        if export_choice == 1:
            list_of_dict_to_csv(database, file_path)
        else:
            list_of_dict_to_json(database, file_path)
            
        functions.clear_screen()
        
        print("Congrats 🎉! Your database is ready.")
        functions.generate_more()
        
if __name__ == "__main__":
    functions.clear_screen()
    print("🌟 Welcome to the Synthetic Data Generation tool! 🌟\n")
    main()