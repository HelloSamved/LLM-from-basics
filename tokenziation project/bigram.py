# bigram_model.py
import random
from tokenizer import build_tokenizer

def train_bigram_model():
    print("--- Starting Step 3: Bigram Model Training ---")
    
    # 1. Get our tokens and encoding/decoding functions from Step 2
    all_tokens, encode, decode = build_tokenizer()
    
    # 2. Build the count matrix using a Python dictionary
    # Structure: { current_token: { next_token: count } }
    bigram_counts = {}
    
    print("\nCounting bigram frequencies across the entire dataset...")
    # Loop through the tokens in pairs: (token1, token2), (token2, token3), etc.
    for t1, t2 in zip(all_tokens[:-1], all_tokens[1:]):
        if t1 not in bigram_counts:
            bigram_counts[t1] = {}
        if t2 not in bigram_counts[t1]:
            bigram_counts[t1][t2] = 0
            
        bigram_counts[t1][t2] += 1

    # 3. Convert counts to probabilities
    # Structure: { current_token: { next_token: probability } }
    bigram_probs = {}
    for t1, t2_counts in bigram_counts.items():
        total_occurrences = sum(t2_counts.values())
        bigram_probs[t1] = { t2: count / total_occurrences for t2, count in t2_counts.items() }

    print("Model training complete!")
    
    # 4. Let's look at a quick statistical sample!
    # Let's check what typically follows the letter 't'
    t_token = encode('t')[0]
    print(f"\nTop 5 tokens most likely to follow 't':")
    sorted_following_t = sorted(bigram_probs[t_token].items(), key=lambda item: item[1], reverse=True)[:5]
    for token_id, prob in sorted_following_t:
        char = decode([token_id])
        # Format space character so it's visible
        display_char = "[space]" if char == " " else char
        print(f"  '{display_char}' (Token {token_id}): {prob:.2%}")

    # 5. GENERATE TEXT!
    # Start with a random token or a specific seed character like 't'
    current_token = encode('t')[0]
    generated_tokens = [current_token]
    
    print("\nGenerating 200 characters of text using our Bigram Model...")
    for _ in range(200):
        if current_token in bigram_probs:
            # Get possible next tokens and their probabilities
            next_choices = list(bigram_probs[current_token].keys())
            next_weights = list(bigram_probs[current_token].values())
            
            # Make a weighted random choice based on our probabilities
            current_token = random.choices(next_choices, weights=next_weights)[0]
        else:
            # Fallback if a token has no recorded history
            current_token = random.choice(all_tokens)
            
        generated_tokens.append(current_token)
        
    print("\n--- GENERATED TEXT ---")
    print(decode(generated_tokens))
    print("----------------------")

if __name__ == "__main__":
    train_bigram_model()