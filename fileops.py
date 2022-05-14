import algorithm
from bitarray import bitarray


def encode_from_file(input_path, output_path, keys):
    with open(input_path, "r") as in_file:
        with open(output_path, "w") as out_file:
            for line in in_file:
                out_file.write(algorithm.triple_des_encryption(line, keys[0], keys[1], keys[2]).to01())


def decode_from_file(input_path, output_path, keys):
    with open(input_path, "r") as in_file:
        with open(output_path, "w") as out_file:
            for line in in_file:
                out_file.write(algorithm.triple_des_decryption(bitarray(line), keys[0], keys[1], keys[2]))
