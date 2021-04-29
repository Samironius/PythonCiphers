import string
import random


alphabet = list(string.ascii_lowercase)
dict_alphabet = dict(zip(list(range(len(alphabet))), alphabet))
text_for_encrypted = open("text.txt", "r").read().lower()
result = open("cipher_result.txt", "w")
generated_keys = open("key.txt", "w")


def convertor(word):
    list_code = []
    for letter in word:
        for index in dict_alphabet:
            if letter == dict_alphabet[index]:
                list_code.append(index)
    return list_code


def encode(text):
    key = ''.join([random.choice(string.ascii_lowercase) for x in range(random.randint(len(text_for_encrypted) - 5, len(text_for_encrypted) + 5))]) + " "
    generated_keys.write(key + "\n")
    convert_encode_list = list(map(sum, zip(convertor(key), convertor(text))))
    encoded_text = ""
    for x in convert_encode_list:
        encoded_text += dict_alphabet[x % len(dict_alphabet)]
    return encoded_text


def recursive_coding(text_for_encrypted, count):
    count -= 1
    encoded = encode(text_for_encrypted)
    print(count, text_for_encrypted, encoded)
    if count > 0:
        return recursive_coding(encoded, count)
    return encoded


result.write(recursive_coding(text_for_encrypted, 5))