"""
Experiment No 2. Develop a program to encode and decode a text file with the LZW
method. Assume ASCII code is the initial dictionary for the character of the text file.
Read the data from a file and write the encoded and decoded data in a separate file.
"""


class LZWEncoderDecoder:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.dictionary = dict((chr(i), i) for i in range(256))

    def encode(self):
        with open(self.input_file_path, 'r') as input_file, open(self.output_file_path, 'wb') as output_file:
            data = input_file.read()
            result = []
            w = ''
            for c in data:
                wc = w + c
                if wc in self.dictionary:
                    w = wc
                else:
                    result.append(self.dictionary[w])
                    self.dictionary[wc] = len(self.dictionary)
                    w = c
            if w:
                result.append(self.dictionary[w])
            output_file.write(bytearray(result))

    def decode(self):
        with open(self.output_file_path, 'rb') as output_file, open(self.input_file_path + '.decoded', 'w') as decoded_file:
            data = output_file.read()
            dictionary = dict((i, chr(i)) for i in range(256))
            result = []
            w = chr(data[0])
            result.append(w)
            for i in range(1, len(data)):
                if data[i] in dictionary:
                    entry = dictionary[data[i]]
                elif data[i] == len(dictionary):
                    entry = w + w[0]
                else:
                    raise ValueError('Bad compressed data')
                result.append(entry)
                dictionary[len(dictionary)] = w + entry[0]
                w = entry
            decoded_file.write(''.join(result))

if __name__ == '__main__':
    input_file_path = 'input.txt'
    output_file_path = 'output.bin'
    encoder_decoder = LZWEncoderDecoder(input_file_path, output_file_path)
    encoder_decoder.encode()
    encoder_decoder.decode()
