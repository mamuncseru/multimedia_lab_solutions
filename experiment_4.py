"""
Experiment No 4. Develop a program to encode a string of characters with the Huffman
coding method. Generate the probability of the symbol of the string automatically. Read
the data from a file and encode it (i.e. write the symbol table and the codeword of the
data) in another file. Also, decode the encoded data in a separate file.
"""

import heapq
import collections
import json

class Node:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

def count_frequency(text):
    frequency_dict = collections.Counter(text)
    return frequency_dict

def build_huffman_tree(frequency_dict):
    heap = [Node(freq, sym) for sym, freq in frequency_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(node1.frequency + node2.frequency, left=node1, right=node2)
        heapq.heappush(heap, merged)

    return heap[0]

def build_symbol_table(node, prefix="", symbol_table={}):
    if node.symbol:
        symbol_table[node.symbol] = prefix
    else:
        build_symbol_table(node.left, prefix+"0", symbol_table)
        build_symbol_table(node.right, prefix+"1", symbol_table)
    return symbol_table

def encode_text(text, symbol_table):
    encoded_text = ""
    for char in text:
        encoded_text += symbol_table[char]
    return encoded_text

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol:
            decoded_text += current_node.symbol
            current_node = huffman_tree

    return decoded_text

def write_encoded_text(encoded_text, symbol_table, output_file):
    with open(output_file, "w") as file:
        for symbol, code in symbol_table.items():
            file.write(f"{symbol}:{code}\n")
        file.write(f"Encoded Text:{encoded_text}\n")

def read_encoded_text(encoded_text_file):
    symbol_table = {}
    encoded_text = ''

    try:
        with open(encoded_text_file, 'r') as f:
            # Read symbol table from first line
            symbol_table_str = f.readline().rstrip()
            symbol_table = json.loads(symbol_table_str)

            # Read encoded text from remaining lines
            for line in f:
                encoded_text += line.rstrip()
    except FileNotFoundError:
        print(f"File not found: {encoded_text_file}")
    
    return symbol_table, encoded_text

def write_decoded_text(decoded_text, output_file):
    with open(output_file, "w") as file:
        file.write(decoded_text)

def main():
    # Read input file
    input_file = "input.txt"
    with open(input_file, "r") as file:
        text = file.read().strip()

    # Build Huffman tree and symbol table
    frequency_dict = count_frequency(text)
    huffman_tree = build_huffman_tree(frequency_dict)
    symbol_table = build_symbol_table(huffman_tree)

    # Encode text and write to file
    encoded_text = encode_text(text, symbol_table)
    encoded_text_file = "encoded_text.txt"
    write_encoded_text(encoded_text, symbol_table, encoded_text_file)

    # Read encoded text and symbol table from file
    symbol_table, encoded_text = read_encoded_text(encoded_text_file)

    # Decode text and write to file
    decoded_text = decode_text(encoded_text, huffman_tree)
    decoded_text_file = "decoded_text.txt"
    write_decoded_text(decoded_text_file)

if __name__ == "__main__":
    main()