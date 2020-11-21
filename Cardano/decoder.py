given_key = [[1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0]]

text_for_decoding = open("cipher_result.txt", "r").read()


def turn(matrix_key):
    turn_matrix = []
    for i in range(len(matrix_key[0])):
        local_matrix = []
        for j in range(-1, -len(matrix_key) - 1, -1):
            local_matrix.append(matrix_key[j][i])
        turn_matrix.append(local_matrix)
    return turn_matrix


def decoding(matrix_key, text_for_decoding):
    text_list = []
    count = len(matrix_key)
    encrypted_matrix = []
    decoding_text = ""
    for splited in range(count, count*count+count, count):
        text_list.append(text_for_decoding[splited - len(matrix_key):splited])
    for encoding_word in text_list:
        encrypted_matrix.append(list(encoding_word))
    for x in range(4):
        for i in range(len(matrix_key)):
            for j in range(len(matrix_key)):
                if matrix_key[i][j] == 1:
                    decoding_text += str(encrypted_matrix[i][j])
        matrix_key = turn(matrix_key)
    return decoding_text.strip(":")


result = open("decoding_result.txt", "w")
result.write(decoding(given_key, text_for_decoding))
result.close()
print(decoding(given_key, text_for_decoding))