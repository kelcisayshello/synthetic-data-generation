from generators import *
from converters import *
import utils
import config

CONTENT_TYPE_MAPPING = {
    1: "books",
    2: "users",
    3: "favorited books",
}

GENERATOR_FUNCTIONS = {
    1: generate_book_data,
    2: generate_user_data,
    3: generate_favoritedbook_data,
}

def main():
    while True:
        user_content_choice = utils.get_content_type()
        content_type = CONTENT_TYPE_MAPPING[user_content_choice]
        
        utils.clear_screen()
            
        content_count = utils.get_content_count(content_type)
        
        utils.update_config_variable_count(content_type, content_count)
        database = []
        generator_function = GENERATOR_FUNCTIONS[user_content_choice]
            
        for _ in range(content_count):
            
            if generator_function == generate_favoritedbook_data:
                content_record = generator_function(config.BOOKS_COUNT)
            else:
                content_record = generator_function()
            database.append(content_record)
            
        utils.clear_screen()
        
        export_choice = utils.get_export_choice()
        file_path = utils.get_output_file_path(export_choice)
        
        if export_choice == 1:
            list_of_dict_to_csv(database, file_path)
        else:
            list_of_dict_to_json(database, file_path)
            
        utils.clear_screen()
        
        print("Congrats 🎉! Your database is ready.")
        utils.generate_more()
        
if __name__ == "__main__":
    utils.clear_screen()
    print("🌟 Welcome to the Synthetic Data Generation tool! 🌟\n")
    main()