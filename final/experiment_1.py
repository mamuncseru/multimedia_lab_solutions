"""
Experiment No 1. Develop a program to encode and decode a text file with the RLE
method. Read the data from a file and write the encoded and decoded data in a separate
file.

"""
class RLEEncoderDecoder:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def encode(self):
        with open(self.input_file_path, 'r') as input_file, open(self.output_file_path, 'w') as output_file:
            data = input_file.read()
            i = 0
            while i < len(data):
                count = 1
                if data[i].isdigit():
                    while i + count < len(data) and data[i + count].isdigit():
                        count += 1
                    output_file.write('N' + str(count) + 'N' + data[i])
                else:
                    while i + count < len(data) and data[i + count] == data[i]:
                        count += 1
                    if count > 1:
                        output_file.write(str(count) + data[i])
                    else:
                        output_file.write(data[i])
                
                i += count

    def decode(self):
        with open(self.output_file_path, 'r') as output_file, open(self.input_file_path + '.decoded', 'w') as decoded_file:
            data = output_file.read()
            i = 0
            while i < len(data):
                if data[i] == 'N':
                    count_str = ''
                    i += 1
                    while data[i] != 'N':
                        count_str += data[i]
                        i += 1
                    count = int(count_str)
                    i += 1
                    decoded_file.write(count * data[i])
                else:
                    count = ''
                    while i < len(data) and data[i].isdigit():
                        count += data[i]
                        i += 1
                    if count:
                        count = int(count)
                        decoded_file.write(count * data[i])
                    else:
                        decoded_file.write(data[i])
                i += 1


if __name__ == '__main__':
    
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    
    encoder_decoder = RLEEncoderDecoder(input_file_path, output_file_path)
    encoder_decoder.encode()
    encoder_decoder.decode()


