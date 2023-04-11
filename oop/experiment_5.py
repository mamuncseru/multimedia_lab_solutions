"""
Experiment No 5. Develop a program to apply DCT on a gray level image 16X16 and
plot the transformed image. Then apply IDCT on the transformed image and plot it also.
"""

import numpy as np
import cv2

class DCT:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.block_size = 16

    def encode(self):
        img = cv2.imread(self.input_file_path, cv2.IMREAD_GRAYSCALE)
        rows, cols = img.shape
        dct_img = np.zeros(img.shape, dtype=np.float32)
        for i in range(0, rows, self.block_size):
            for j in range(0, cols, self.block_size):
                block = np.float32(img[i:i+self.block_size, j:j+self.block_size])
                dct_block = cv2.dct(block)
                dct_img[i:i+self.block_size, j:j+self.block_size] = dct_block
        cv2.imwrite(self.output_file_path, dct_img)

    def decode(self):
        dct_img = cv2.imread(self.output_file_path, cv2.IMREAD_GRAYSCALE)
        rows, cols = dct_img.shape
        img = np.zeros(dct_img.shape, dtype=np.uint8)
        for i in range(0, rows, self.block_size):
            for j in range(0, cols, self.block_size):
                dct_block = np.float32(dct_img[i:i+self.block_size, j:j+self.block_size])
                block = cv2.idct(dct_block)
                img[i:i+self.block_size, j:j+self.block_size] = np.uint8(block)
        cv2.imwrite(self.input_file_path + '.decoded.jpg', img)

if __name__ == '__main__':
    input_file_path = 'input.jpg'
    output_file_path = 'output.jpg'
    dct = DCT(input_file_path, output_file_path)
    dct.encode()
    dct.decode()
