# Synthetic Data Generation 🤖

This project offers a flexible solution for generating customizable fake data, empowering other developers to enhance web applications, software, and machine learning projects with no-bloat tools for development.

### File Structure 📑

```
.
├── converters/
│   ├── to_json.py
│   └── to_csv.py
├── generators/
│   ├── Book.py
│   ├── FavoriteBook.py
│   ├── User.py
│   └── Author.py
├── sample_outputs/
│   └── ghost_file.txt
├── virtualenv/
├── .gitignore
├── config.py
├── dialogue.py
├── README.md
├── requirements.txt
└── utils.py
```

### Up-To-Date Modules

`generators/`: Core modules for generating structured data for the application.
* `Book.py`: Contains data generation logic for book objects, including titles, authors, genres, and other relevant metadata.
* `FavoritedBook.py`: Handles data generation specific to user-favorited books, including relationships between users and book objects.
* `User.py`: Contains data generation for user profiles, such as usernames, passwords, email addresses, and other user-specific information.
* `Author.py`: Contains data generation for book author profiles, including name, biography, birth date and death date (if exists).

### Getting Started 🚀

1. Clone the repository.
2. Create and activate a virtual environment.
```zsh
python3 -m venv virtualenv
source virtualenv/bin/activate
```
3. Install Python dependencies.
```zsh
pip install -r requirements.txt
```
4. From the root folder, run the `dialogue.py` file using this command and follow the terminal workflow.
```zsh
python3 dialogue.py
```
5. That's it! To exit the data generation program, enter `CTRL` + `C` at any time. Happy data generating!

### Sample Data Generation Workflow ✨
<!-- ![](preview_dialogue.gif) -->
( .gif preview coming soon )