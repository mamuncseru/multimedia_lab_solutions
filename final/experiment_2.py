"""
Experiment No 2. Develop a program to encode and decode a text file with the LZW
method. Assume ASCII code is the initial dictionary for the character of the text file.
Read the data from a file and write the encoded and decoded data in a separate file.

"""

class LZWEncoderDecoder:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def encode(self):
        with open(self.input_file_path, 'r') as input_file, open(self.output_file_path, 'w') as output_file:
            data = input_file.read()
            dictionary = {chr(i): i for i in range(256)}
            next_code = 256
            current_string = data[0]
            for symbol in data[1:]:
                if current_string + symbol in dictionary:
                    current_string = current_string + symbol
                else:
                    output_file.write(str(dictionary[current_string]) + ' ')
                    dictionary[current_string + symbol] = next_code
                    next_code += 1
                    current_string = symbol
            output_file.write(str(dictionary[current_string]))

    def decode(self):
        with open(self.output_file_path, 'r') as output_file, open(self.input_file_path + '.decoded', 'w') as decoded_file:
            data = output_file.read().split()
            dictionary = {i: chr(i) for i in range(256)}
            next_code = 256
            current_code = int(data[0])
            decoded_data = dictionary[current_code]
            previous_string = decoded_data
            for code in data[1:]:
                code = int(code)
                if code in dictionary:
                    current_string = dictionary[code]
                else:
                    current_string = previous_string + previous_string[0]
                decoded_data += current_string
                dictionary[next_code] = previous_string + current_string[0]
                next_code += 1
                previous_string = current_string
            decoded_file.write(decoded_data)


if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    encoder_decoder = LZWEncoderDecoder(input_file_path, output_file_path)
    encoder_decoder.encode()
    encoder_decoder.decode()
