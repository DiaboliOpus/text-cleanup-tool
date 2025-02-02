# Text Cleanup and Cryptanalysis Tool

This script processes and cleans text files by removing HTML tags, punctuation, and digits, converting text to lowercase, and removing extra spaces. Additionally, it performs frequency analysis on Kazakh text, including letter, bigram, and trigram frequency counts, and constructs a Vigenère square.

## Features
✅ Cleans raw text by removing unnecessary characters.
✅ Performs frequency analysis on:
   - Single letters
   - Bigrams (two-letter combinations)
   - Trigrams (three-letter combinations)
✅ Generates and saves a **Vigenère square**.
✅ Outputs data in CSV format for further analysis.

## Requirements
Before running the script, ensure you have the required dependencies installed. Install them using pip:

```bash
pip install beautifulsoup4 pandas matplotlib
```

## Usage
1. Place raw text files in the `raw_texts` directory.
2. Run the script using:

```bash
python text_cleanup.py
```

3. Cleaned text files will be saved in the `clean_texts` directory.
4. Frequency analysis results and the Vigenère square will be generated in CSV format.

## Output Files
After running the script, you will find:
- `letter_frequency.csv` → Letter frequency results
- `bigram_frequency.csv` → Bigram frequency results
- `trigram_frequency.csv` → Trigram frequency results
- `vigenere_square.csv` → Vigenère square table

## Repository Structure
```
/text_cleanup_project
├── text_cleanup.py      # Main script
├── raw_texts/           # Folder for raw text files
├── clean_texts/         # Folder for cleaned text files
├── letter_frequency.csv # Letter frequency results
├── bigram_frequency.csv # Bigram frequency results
├── trigram_frequency.csv # Trigram frequency results
├── vigenere_square.csv  # Vigenère square table
└── README.md            # Documentation file
```

## License
This project is licensed under the MIT License.
