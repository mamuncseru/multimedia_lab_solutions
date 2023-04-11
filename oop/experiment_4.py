"""
Experiment No 4. Develop a program to encode a string of characters with the Huffman
coding method. Generate the probability of the symbol of the string automatically. Read
the data from a file and encode it (i.e. write the symbol table and the codeword of the
data) in another file. Also, decode the encoded data in a separate file.
"""

from heapq import heappush, heappop
from collections import defaultdict

# define a class to represent a Huffman node
class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# define a function to generate the Huffman tree
def generate_tree(probabilities):
    heap = []
    for symbol, probability in probabilities.items():
        node = Node(symbol=symbol, frequency=probability)
        heappush(heap, node)

    while len(heap) > 1:
        left_child = heappop(heap)
        right_child = heappop(heap)
        parent = Node(frequency=left_child.frequency + right_child.frequency)
        parent.left_child = left_child
        parent.right_child = right_child
        heappush(heap, parent)

    return heap[0]

# define a function to generate the Huffman codes
def generate_codes(root_node):
    codes = {}
    def traverse(node, code):
        if node is None:
            return
        if node.symbol is not None:
            codes[node.symbol] = code
        traverse(node.left_child, code + '0')
        traverse(node.right_child, code + '1')
    traverse(root_node, '')
    return codes

# define a class to perform Huffman coding
class HuffmanCoder:
    def __init__(self, text):
        self.text = text
        self.probabilities = self.calculate_probabilities(text)
        self.tree = generate_tree(self.probabilities)
        self.codes = generate_codes(self.tree)

    def calculate_probabilities(self, text):
        counts = defaultdict(int)
        for symbol in text:
            counts[symbol] += 1
        probabilities = {}
        for symbol, count in counts.items():
            probabilities[symbol] = count / len(text)
        return probabilities

    def encode(self):
        encoded_data = ''
        for symbol in self.text:
            encoded_data += self.codes[symbol]
        return encoded_data

    def decode(self, encoded_data):
        decoded_data = ''
        current_node = self.tree
        for bit in encoded_data:
            if bit == '0':
                current_node = current_node.left_child
            elif bit == '1':
                current_node = current_node.right_child
            if current_node.symbol is not None:
                decoded_data += current_node.symbol
                current_node = self.tree
        return decoded_data

# read the data from the input file
with open("input.txt", "r") as input_file:
    data = input_file.read().strip()

# encode the data with Huffman coding and write to output file
coder = HuffmanCoder(data)
encoded_data = coder.encode()
with open("encoded_output.txt", "w") as encoded_file:
    for symbol, code in coder.codes.items():
        encoded_file.write(f"{symbol}: {code}\n")
    encoded_file.write(encoded_data)

# decode the encoded data with Huffman coding and write to output file
decoded_data = coder.decode(encoded_data)
with open("decoded_output.txt", "w") as decoded_file:
    decoded_file.write(decoded_data)
