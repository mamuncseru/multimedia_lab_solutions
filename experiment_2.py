"""
Experiment No 2. Develop a program to encode and decode a text file with the LZW
method. Assume ASCII code is the initial dictionary for the character of the text file.
Read the data from a file and write the encoded and decoded data in a separate file.
"""

# define a function to encode the data with LZW
def encode_LZW(data):
    # create the initial dictionary with ASCII characters
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # initialize variables for encoding
    current_string = data[0]
    encoded_data = []
    
    for symbol in data[1:]:
        if current_string + symbol in dictionary:
            current_string = current_string + symbol
        else:
            encoded_data.append(dictionary[current_string])
            dictionary[current_string + symbol] = next_code
            next_code += 1
            current_string = symbol
    
    # add the last code to the encoded data
    encoded_data.append(dictionary[current_string])
    
    return encoded_data

# define a function to decode the data with LZW
def decode_LZW(data):
    # create the initial dictionary with ASCII characters
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # initialize variables for decoding
    current_code = data[0]
    decoded_data = dictionary[current_code]
    previous_string = decoded_data
    
    for code in data[1:]:
        if code in dictionary:
            current_string = dictionary[code]
        else:
            current_string = previous_string + previous_string[0]
        decoded_data += current_string
        
        # add the new entry to the dictionary
        dictionary[next_code] = previous_string + current_string[0]
        next_code += 1
        
        previous_string = current_string
    
    return decoded_data

# read the data from the input file
with open("input.txt", "r") as input_file:
    data = input_file.read().strip()

# encode the data with LZW and write to output file
encoded_data = encode_LZW(data)
with open("encoded_output.txt", "w") as encoded_file:
    for code in encoded_data:
        encoded_file.write(str(code) + " ")

# decode the data with LZW and write to output file
decoded_data = decode_LZW(encoded_data)
with open("decoded_output.txt", "w") as decoded_file:
    decoded_file.write(decoded_data)
