from bitarray import bitarray


# exclusive or operation on two binary strings
def xor(bits1, bits2):
    result = bitarray()
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]:
            result.append(0)
        else:
            result.append(1)
    return result


# dividing an input string into equally sized chunks
# (last chunk can be shorter when the input's length isn't wholely divided by chunk size)
def split_string_into_chunks(to_split, chunk_size):
    how_many_chunks = len(to_split) // chunk_size
    left_over = len(to_split) % chunk_size
    index = 0
    text_chunks = list()
    chunk = ""
    for i in range(how_many_chunks):
        for j in range(chunk_size):
            chunk += to_split[index]
            index += 1
        text_chunks.append(chunk)
        chunk = ""
    if left_over != 0:
        for i in range(left_over):
            chunk += to_split[index + i]
        text_chunks.append(chunk)
    return text_chunks


def split_bitarray_into_chunks(to_split, chunk_size):
    how_many_chunks = len(to_split) // chunk_size
    left_over = len(to_split) % chunk_size
    index = 0
    list_of_xbits = list()
    chunk = bitarray()
    for i in range(how_many_chunks):
        for j in range(chunk_size):
            chunk.append(to_split[index])
            index += 1
        list_of_xbits.append(chunk.copy())
        chunk.clear()
    if left_over != 0:
        for i in range(left_over):
            chunk.append(to_split[index+i])
        list_of_xbits.append(chunk.copy())

    return list_of_xbits


# left shift the bits of input by specified number of bits
def shift(key, number_of_bits):
    shifted_key = bitarray()
    i = 0
    while i < number_of_bits:
        shifted_key.append(key[i])
        i = i + 1
    i = 0
    while number_of_bits < len(key):
        key[i] = key[number_of_bits]
        i = i + 1
        number_of_bits = number_of_bits + 1
    key[:] = key[: i] + shifted_key

    return key


# divide input string into equal halves
def split_in_half(to_split):
    half_length = int(len(to_split) / 2)
    l_half, r_half = to_split[:half_length], to_split[half_length:]
    return l_half, r_half
