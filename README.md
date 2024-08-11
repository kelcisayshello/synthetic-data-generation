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
```
python3 -m venv virtualenv
source virtualenv/bin/activate
```
3. Install Python dependencies
```
pip install -r requirements.txt
```
4. Run the data generation scripts in the `generators/` folder.
5. Convert the generated data using the scripts in the `converters/` folder.

### Example Code ✨ to Generate Synthetic Book Data

```python
from generators import *

# Generate data for a single book
book_data = generate_book_data(1)
print(book_data)

# Generate data for multiple books
num_books = 10
book_data_list = [generate_book_data(i+1) for i in range(num_books)] 

# Save data to a JSON file
import json
with open('sample_book_data.json', 'w') as f:
    json.dump(book_data_list, f, indent=4)
```