# Synthetic Data Generation 🤖

I understand the importance of having quality synthetic data for testing, development, and machine learning projects. Thus this project was created to be a reusable resource for generating realistic, customizable, but fake media data. 

### File Structure 📑

* `generators/`: Contains the core data generation logic.
    * `books.py`: Functions used to generate fake book data.
* `converters/`: Provides utilities to convert generated data into different formats.
    * `to_json.py`: Converts data to JSON format.
    * `to_csv.py`: Converts data to CSV format.
* `sample_outputs/`: Stores examples of generated data in various formats.
* `README.md`: This file! 👋

### Getting Started 🚀

1. Clone the repository
2. Create and activate a virtual environment
```zsh
python3 -m venv virtualenv
source virtualenv/bin/activate
```
3. Install Python dependencies
```zsh
pip install -r requirements.txt
```
4. From the root folder, run the `main.py` file using this command.
```zsh
python3 main.py
```
5. Happy data generation!

### Sample Data Generation Workflow ✨
(Preview coming soon . . . !)