given_key = [[1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0]]

text_for_encrypted = open("text.txt", "r").read()


def turn(matrix_key):
    turn_matrix = []
    for i in range(len(matrix_key[0])):
        local_matrix = []
        for j in range(-1, -len(matrix_key) - 1, -1):
            local_matrix.append(matrix_key[j][i])
        turn_matrix.append(local_matrix)
    return turn_matrix


def create_empty_matrix(matrix_key):
    empty_matrix = []
    for i in range(len(matrix_key)):
        empty_matrix.append([":" for x in range(len(matrix_key))])
    return empty_matrix


def encryption(matrix_key, text_for_encrypted):
    encrypted_matrix = create_empty_matrix(matrix_key)
    index = 0
    for count in range(4):
        for i in range(len(matrix_key)):
            for j in range(len(matrix_key)):
                if matrix_key[i][j] == 1 and len(text_for_encrypted) > index:
                    encrypted_matrix[i][j] = text_for_encrypted[index]
                    index += 1
        matrix_key = turn(matrix_key)
    encrypted_text = ""
    for row in encrypted_matrix:
        for items in row:
            encrypted_text += str(items)
    return encrypted_text


result = open("cipher_result.txt", "w")
result.write(encryption(given_key, text_for_encrypted))
result.close()
print(encryption(given_key ,text_for_encrypted))
