import re
import os
import string
from bs4 import BeautifulSoup

def clean_text(text):
    # Удаление HTML-разметки
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Удаление пунктуации и цифр
    text = re.sub(r"[\d" + re.escape(string.punctuation) + "]", "", text)
    
    # Приведение к нижнему регистру
    text = text.lower()
    
    # Удаление лишних пробелов
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

def process_files(input_folder, output_folder):
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
                
            print(f"Обработан файл: {filename}")

if __name__ == "__main__":
    input_folder = "raw_texts"  # Папка с сырыми текстами
    output_folder = "clean_texts"  # Папка с очищенными текстами
    process_files(input_folder, output_folder)
    print("Очистка завершена!")
