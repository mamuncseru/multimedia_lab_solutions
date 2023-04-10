'''
Experiment No 1. Develop a program to encode and decode a text file with the RLE
method. Read the data from a file and write the encoded and decoded data in a separate
file.
'''

# define a function to encode the data with RLE
def encode_RLE(data):
    encoded_data = ""
    count = 1
    character = data[0]
    for i in range(1, len(data)):
        if data[i] == character:
            count += 1
        else:
            encoded_data += str(count) + character
            count = 1
            character = data[i]
    encoded_data += str(count) + character
    return encoded_data

# define a function to decode the data with RLE
def decode_RLE(data):
    decoded_data = ""
    count = ""
    for i in data:
        if i.isdigit():
            count += i
        else:
            decoded_data += int(count) * i
            count = ""
    return decoded_data

# read the data from the input file
with open("input.txt", "r") as input_file:
    data = input_file.read().strip()

print('hello')
# encode the data with RLE and write to output file
encoded_data = encode_RLE(data)
with open("encoded_output.txt", "w") as encoded_file:
    print('hi')
    encoded_file.write(encoded_data)

# decode the data with RLE and write to output file
decoded_data = decode_RLE(encoded_data)
with open("decoded_output.txt", "w") as decoded_file:
    decoded_file.write(decoded_data)
