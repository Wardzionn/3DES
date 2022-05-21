import algorithm
from bitarray import bitarray


def encode_from_file(input_path, output_path, keys):
    try:
        with open(input_path, "r") as in_file:
            with open(output_path, "wb") as out_file:
                for line in in_file:
                    bitarray(algorithm.triple_des_encryption(line, keys[0], keys[1], keys[2])).tofile(out_file)
                    #out_file.write(algorithm.triple_des_encryption(line, keys[0], keys[1], keys[2]).to01())
    except FileNotFoundError:
        print("File path is incorrect!")


def decode_from_file(input_path, output_path, keys):
    try:
        with open(input_path, "rb") as in_file:
            with open(output_path, "w") as out_file:
                bit_line = bitarray()
                bit_line.fromfile(in_file)
                #for line in in_file:

                out_file.write(algorithm.triple_des_decryption(bit_line, keys[0], keys[1], keys[2]))
    except FileNotFoundError:
        print("File path is incorrect!")
