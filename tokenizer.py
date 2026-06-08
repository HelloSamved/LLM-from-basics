# tokenizer.py

CLEAN_FILENAME = 'clean_data.txt'

def build_tokenizer():
    print("--- Starting Step 2: Tokenization ---")
    
    # 1. Read the cleaned text
    with open(CLEAN_FILENAME, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # 2. Find all unique characters (the vocabulary)
    # Using set() automatically removes all duplicates
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    
    print(f"Total characters in dataset: {len(text)}")
    print(f"Vocabulary size (unique characters found): {vocab_size}")
    print(f"The vocabulary: {''.join(chars)}\n")
    
    # 3. Create mapping dictionaries
    # stoi: string-to-integer mapping
    stoi = { ch:i for i,ch in enumerate(chars) }
    # itos: integer-to-string mapping
    itos = { i:ch for i,ch in enumerate(chars) }
    
    # 4. Define the encode and decode functions
    # encode: take a string, output a list of integers
    encode = lambda s: [stoi[c] for c in s]
    # decode: take a list of integers, output a string
    decode = lambda l: ''.join([itos[i] for i in l])
    
    # 5. Let's test it out on a sample sentence!
    sample_phrase = "hello shakespeare"
    encoded_sample = encode(sample_phrase)
    decoded_sample = decode(encoded_sample)
    
    print("--- Tokenizer Test Run ---")
    print(f"Original Text: '{sample_phrase}'")
    print(f"Encoded (Tokens): {encoded_sample}")
    print(f"Decoded Back:   '{decoded_sample}'")
    
    # 6. Now let's encode our entire clean dataset into tokens!
    print("\nTokenizing the entire clean_data.txt file...")
    all_tokens = encode(text)
    
    # Print the first 50 tokens as a sneak peek
    print(f"First 50 tokens of your dataset:\n{all_tokens[:50]}")
    
    return all_tokens, encode, decode

if __name__ == "__main__":
    build_tokenizer()