import re
import os
import string
import collections
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def clean_text(text):
    """Cleans the input text by removing HTML tags, punctuation, digits, and extra spaces."""
    text = BeautifulSoup(text, "html.parser").get_text()  # Remove HTML tags
    text = re.sub(r"[\d" + re.escape(string.punctuation) + "]", "", text)  # Remove punctuation and digits
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

def process_files(input_folder, output_folder):
    """Processes all text files in the input folder and saves cleaned versions in the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        if os.path.isfile(input_path):
            with open(input_path, "r", encoding="utf-8") as file:
                text = file.read()
            
            cleaned_text = clean_text(text)
            
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(cleaned_text)
                
            print(f"Processed file: {filename}")

def frequency_analysis(text):
    """Performs frequency analysis on single letters, bigrams, and trigrams."""
    letter_counts = collections.Counter(text)
    bigram_counts = collections.Counter([text[i:i+2] for i in range(len(text)-1)])
    trigram_counts = collections.Counter([text[i:i+3] for i in range(len(text)-2)])
    
    return letter_counts, bigram_counts, trigram_counts

def generate_vigenere_square(alphabet):
    """Generates the Vigenère square for a given alphabet."""
    size = len(alphabet)
    square = [[alphabet[(i + j) % size] for j in range(size)] for i in range(size)]
    return square

def save_vigenere_square(square, filename="vigenere_square.csv"):
    """Saves the Vigenère square as a CSV file."""
    df = pd.DataFrame(square)
    df.to_csv(filename, index=False, header=False)
    print(f"Vigenère square saved to {filename}")

if __name__ == "__main__":
    input_folder = "raw_texts"  # Folder containing raw text files
    output_folder = "clean_texts"  # Folder for cleaned text files
    process_files(input_folder, output_folder)
    print("Text cleaning completed!")
    
    # Collect all cleaned text
    all_text = ""
    for filename in os.listdir(output_folder):
        with open(os.path.join(output_folder, filename), "r", encoding="utf-8") as file:
            all_text += file.read()
    
    # Perform frequency analysis
    letter_freq, bigram_freq, trigram_freq = frequency_analysis(all_text)
    print("Frequency analysis completed!")
    
    # Save results to CSV
    pd.DataFrame(letter_freq.most_common(), columns=["Letter", "Count"]).to_csv("letter_frequency.csv", index=False)
    pd.DataFrame(bigram_freq.most_common(), columns=["Bigram", "Count"]).to_csv("bigram_frequency.csv", index=False)
    pd.DataFrame(trigram_freq.most_common(), columns=["Trigram", "Count"]).to_csv("trigram_frequency.csv", index=False)
    
    print("Frequency analysis results saved!")
    
    # Generate and save Vigenère square
    kazakh_alphabet = "аәбвгғдежзийкқлмңноөпрстуүфхһцчшщъыіьэюя"
    vigenere_square = generate_vigenere_square(kazakh_alphabet)
    save_vigenere_square(vigenere_square)
