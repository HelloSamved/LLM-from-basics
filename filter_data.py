import os
import urllib.request

# The direct link to the raw data
DATA_URL = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
RAW_FILENAME = 'raw_data.txt'
CLEAN_FILENAME = 'clean_data.txt'

def download_data():
    if not os.path.exists(RAW_FILENAME):
        print(f"Downloading raw data from {DATA_URL}...")
        urllib.request.urlretrieve(DATA_URL, RAW_FILENAME)
        print("Download complete!")
    else:
        print("Raw data already exists. Skipping download.")

def clean_data():
    print("\n--- Starting Data Filtering ---")
    
    cleaned_lines = []
    
    with open(RAW_FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            # Strip whitespace from the beginning and end of the line
            line = line.strip()
            
            # Filter: If the line is empty after stripping, ignore it
            if line:
                cleaned_lines.append(line)
                
    # Join the lines back together with a space
    final_text = " ".join(cleaned_lines)
    
    with open(CLEAN_FILENAME, "w", encoding="utf-8") as f:
        f.write(final_text)
        
    print(f"Success! Filtered {len(cleaned_lines)} lines of text.")
    print(f"Cleaned data saved to '{CLEAN_FILENAME}'")
    print(f"Total characters in clean data: {len(final_text)}")

if __name__ == "__main__":
    download_data()
    clean_data()