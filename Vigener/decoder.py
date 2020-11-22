import string
import numpy


alphabet = list(string.ascii_lowercase)
dict_alphabet = dict(zip(list(range(len(alphabet))), alphabet))
text_for_decoding = open("cipher_result.txt", "r").read()
key_list = open("key.txt", "r").read().split()
result = open("decoding_result.txt", "w")


def convertor(word):
    list_code = []
    for letter in word:
        for index in dict_alphabet:
            if letter == dict_alphabet[index]:
                list_code.append(index)
    return list_code


def encode(key, code):
    convert_decoded_list = [numpy.subtract(couple[1], couple[0]) for couple in zip(convertor(key), convertor(code))]
    encoded_text = ""
    for x in convert_decoded_list:
        encoded_text += dict_alphabet[x % len(dict_alphabet)]
    return encoded_text


def recursive_coding(text_for_decoding, key_list, count):
    count -= 1
    encoded = encode(key_list[count], text_for_decoding)
    print(count, text_for_decoding, encoded, key_list[count])
    if count > 0:
        return recursive_coding(encoded, key_list, count)
    return encoded


result.write(recursive_coding(text_for_decoding, key_list, len(key_list)))