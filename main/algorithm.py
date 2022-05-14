import tables
import permutation
import convert
import bitops
import random
import string
from bitarray import bitarray


# generate random keys
def random_keys():
    keys = list()
    while len(keys) < 3:
        keys.append(''.join(random.choices(string.ascii_letters + string.digits, k=8)))
    return keys


# generates a list of keys for each round based on supplied keys
def generate_keys(key64):
    keys = list()
    key56 = permutation.basic(tables.PC1, key64)
    left, right = bitops.split_in_half(key56)
    for roundnumber in range(16):
        newL = bitops.shift(left, tables.round_shifts[roundnumber])
        newR = bitops.shift(right, tables.round_shifts[roundnumber])
        key48 = permutation.basic(tables.PC2, newL + newR)
        keys.append(key48)
        left = newL
        right = newR
    return keys


# function used during each round of the algorithm on the current left half of input
def f_function(input32, key48):
    prepare48 = permutation.basic(tables.EXPANSION_TABLE, input32)
    prepare48 = bitops.xor(prepare48, key48)
    prepared32 = permutation.sbox(prepare48)
    result = permutation.basic(tables.PERMUTATION_TABLE, prepared32)
    return result


# main algorithm - only accepts 64 bit chunks of input data
def des(message, key, mode):
    if mode == "e":
        message = convert.ascii_to_bin(message)
    bin_key = convert.ascii_to_bin(key)
    all_keys = generate_keys(bin_key)
    permutated_text = permutation.basic(tables.INITIAL_PERMUTATION_TABLE, message)
    left, right = bitops.split_in_half(permutated_text)
    for i in range(16):
        if mode == "e":
            new_r = bitops.xor(left, f_function(right, all_keys[i]))
        else:
            new_r = bitops.xor(left, f_function(right, all_keys[15 - i]))
        new_l = right
        right = new_r
        left = new_l
    result = permutation.basic(tables.INVERSE_PERMUTATION_TABLE, right + left)
    if mode == "d":
        result = convert.bin_to_ascii(result)
    return result


def triple_des_encryption(message, key1, key2, key3):
    encoded = bitarray()
    chunks64 = bitops.split_string_into_chunks(message, 8)
    padding_counter = 0
    while len(chunks64[-1]) < 8:
        chunks64[-1] += '0'
        padding_counter += 1
    # save number of added padding chars into a 64bit string so that it can be added to the input message and encrypted with it
    padding_counter = str(padding_counter) + '0000000'
    chunks64.insert(0, padding_counter)
    for i in range(len(chunks64)):
        chunks64[i] = des(chunks64[i], key1, "e")
        chunks64[i] = des(chunks64[i], key2, "d")
        chunks64[i] = des(chunks64[i], key3, "e")
        encoded += chunks64[i]
    return encoded


def triple_des_decryption(encoded, key1, key2, key3):
    chunks64 = bitops.split_bitarray_into_chunks(encoded, 64)
    decoded = ""
    for i in range(len(chunks64)):
        chunks64[i] = des(chunks64[i], key3, "d")
        chunks64[i] = des(chunks64[i], key2, "e")
        chunks64[i] = des(chunks64[i], key1, "d")
        decoded += chunks64[i]
    padding_counter = decoded[:8]
    for i in range(int(padding_counter[0])):
        decoded = decoded[:-1]
    decoded = decoded[8:]
    return decoded
