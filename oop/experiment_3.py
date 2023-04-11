"""
Experiment No 3. Develop a program to encode and decode a string of characters with
the arithmetic coding method. Generate the probability of the symbol of the string
automatically. Read the data from a file and write the encoded and decoded data in a
separate file.
"""


import numpy as np

# define a function to calculate the probability of each symbol
def calculate_probabilities(text):
    unique_chars, counts = np.unique(list(text), return_counts=True)
    probabilities = counts / len(text)
    return dict(zip(unique_chars, probabilities))

# define a class to perform arithmetic coding
class ArithmeticCoder:
    def __init__(self, text):
        self.text = text
        self.probabilities = calculate_probabilities(text)
    
    def encode(self, precision=32):
        lower_bound = 0
        upper_bound = 1
        for symbol in self.text:
            symbol_prob = self.probabilities[symbol]
            new_lower_bound = lower_bound + (upper_bound - lower_bound) * 0
            new_upper_bound = lower_bound + (upper_bound - lower_bound) * symbol_prob
            lower_bound = new_lower_bound
            upper_bound = new_upper_bound
        
        code = np.round((lower_bound + upper_bound) / 2, precision)
        return code
    
    def decode(self, code, length, precision=32):
        decoded_text = ''
        lower_bound = 0
        upper_bound = 1
        for i in range(length):
            for symbol, symbol_prob in self.probabilities.items():
                new_lower_bound = lower_bound + (upper_bound - lower_bound) * 0
                new_upper_bound = lower_bound + (upper_bound - lower_bound) * symbol_prob
                if new_lower_bound <= code < new_upper_bound:
                    decoded_text += symbol
                    lower_bound = new_lower_bound
                    upper_bound = new_upper_bound
                    break
        
        return decoded_text

# read the data from the input file
with open("input.txt", "r") as input_file:
    data = input_file.read().strip()

# encode the data with arithmetic coding and write to output file
coder = ArithmeticCoder(data)
encoded_data = coder.encode()
with open("encoded_output.txt", "w") as encoded_file:
    encoded_file.write(str(encoded_data))

# decode the data with arithmetic coding and write to output file
decoded_data = coder.decode(encoded_data, len(data))
with open("decoded_output.txt", "w") as decoded_file:
    decoded_file.write(decoded_data)
