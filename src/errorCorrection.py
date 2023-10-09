import numpy as np

def generate_error_correction_bits(data, error_correction):

    # Calculate the total number of data codewords
    total_data_codewords = 208 - 16 * 1

    # Define the generator polynomial for error correction
    generator_polynomial = np.array([1, 0, 25, 1, 239, 168, 11, 26, 255, 94, 186, 223, 224, 19, 110, 152, 41, 143, 134, 38, 12, 74], dtype=np.uint8)

    # Encode the data using Reed-Solomon error correction
    data_codewords = [ord(c) for c in data] + [0] * 7
    remainder = np.array(data_codewords, dtype=np.uint8)

    for _ in range(total_data_codewords):
        if remainder[0] == 0:
            remainder = remainder[1:]
        else:
            factor = np.multiply(remainder[0], generator_polynomial, dtype=np.uint8)
            remainder = np.concatenate((remainder, np.zeros(factor.shape[0] - remainder.shape[0])))
            remainder = np.array(remainder, dtype=int)
            factor = np.array(factor, dtype=int)
            remainder = np.bitwise_xor(remainder, factor)

    # Add the error correction codewords to the data codewords
    error_correction_codewords = list(remainder)
    data_codewords += error_correction_codewords

    # Convert the codewords to binary and return them
    error_correction_bits = []
    for codeword in data_codewords:
        binary_codeword = bin(codeword)[2:].zfill(8)
        error_correction_bits.extend(map(int, binary_codeword))

    return error_correction_bits



error_correction_bits = generate_error_correction_bits("TEST", "L")

out = ""

for i in error_correction_bits:
    out += str(i)

print(out)