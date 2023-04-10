"""
Experiment No 3. Develop a program to encode and decode a string of characters with
the arithmetic coding method. Generate the probability of the symbol of the string
automatically. Read the data from a file and write the encoded and decoded data in a
separate file.
"""

import numpy as np

def probability_distribution(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    total_count = sum(char_count.values())
    return {char: count/total_count for char, count in char_count.items()}

def arithmetic_encoding(text, probabilities):
    lo, hi = 0.0, 1.0
    for char in text:
        p = probabilities[char]
        range_size = hi - lo
        hi = lo + range_size * p
        lo = lo + range_size * sum(probabilities[c] for c in probabilities if c < char)
    return (lo+hi)/2

def arithmetic_decoding(encoded_text, probabilities, text_length):
    decoded_text = ''
    lo, hi = 0.0, 1.0
    range_size = 1.0

    for i in range(text_length):
        # Calculate the range for the symbol
        symbol_range = hi - lo
        cumulative_prob = 0.0
        for symbol, prob in probabilities.items():
            if symbol_range * cumulative_prob <= encoded_text - lo < symbol_range * (cumulative_prob + prob):
                decoded_text += symbol
                # Update range and scale values
                lo = lo + symbol_range * cumulative_prob
                hi = lo + symbol_range * prob
                range_size = hi - lo
                break
            cumulative_prob += prob
        
        # Check for division by zero
        if range_size == 0:
            break
    
    return decoded_text


def encode_decode(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        text = f.read()
    probabilities = probability_distribution(text)
    encoded_text = arithmetic_encoding(text, probabilities)
    text_length = len(text)
    decoded_text = arithmetic_decoding(encoded_text, probabilities, text_length)
    with open(output_file_path, 'w') as f:
        f.write(decoded_text)

if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    encode_decode(input_file_path, output_file_path)
