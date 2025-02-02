# Text Cleanup Script

This script processes and cleans text files by removing HTML tags, punctuation, and digits, converting text to lowercase, and removing extra spaces. It is designed to work with raw text files stored in a specified directory and outputs the cleaned text to another directory.

## Requirements

Before running the script, ensure you have the required dependencies installed. You can install them using pip:

```bash
pip install beautifulsoup4
```

## Usage

1. Place raw text files in the `raw_texts` directory.
2. Run the script using:

```bash
python text_cleanup.py
```

3. Cleaned text files will be saved in the `clean_texts` directory.
