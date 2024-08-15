import re
import functions

# ---------------------------------------------------------------------------- #
#                 ENVIRONMENT CONFIGURATION VARIABLES (PUBLIC)                 #
# ---------------------------------------------------------------------------- #

BOOKS_COUNT = 30
FAVORITE_BOOKS_COUNT = 2
USERS_COUNT = 0
AUTHORS_COUNT = 20

# ------------------------------------- - ------------------------------------ #

def reset_config():
    """Resets all variables found in this config file back to 0 after user confirmation."""

    functions.clear_screen()
    
    while True:
        try:
            confirmation = input("Hey! You're about to reset your environment. This reverts memory of all variables stored in config.py back to zero.\nAre you sure?\n\n[Y] Yes, reset my environment.\n[N] No, cancel the reset.\n\nEnter your choice: ")
            if confirmation.lower() == 'y' or confirmation.lower() == 'n':
                if confirmation.lower() == 'n':
                    print("❌ Reset has been cancelled.")
                    return
                else:
                    with open("config.py", "r") as config_file:
                        lines = config_file.readlines()

                    with open("config.py", "w") as config_file:
                        for line in lines:
                            match = re.match(r"(\w+)\s*=\s*(.*)", line)
                            if match:
                                variable_name = match.group(1)
                                config_file.write(f"{variable_name} = 0\n")
                            else:
                                config_file.write(line)
                print("Done ✅. Your environment has been reset.")
                return
            else:
                print("Sorry, that was an invalid choice. Please enter either a [y] or [n].\n")
        except ValueError:
            functions.value_error()
                  
if __name__ == "__main__":
    reset_config()