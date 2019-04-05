# Edit Distance 2
def edit_distance(arg1, arg2):
    string1 = "*" + arg1
    string2 = "*" + arg2

    matrix = [[0 for i in range(len(string2))] for j in range(len(string1))]
    parent = [[-1 for i in range(len(string2))] for j in range(len(string1))]
    temp = [0] * 3

    initialize_matrix(matrix, False)
    initialize_matrix(parent, True)

    for i in range(1,len(string1)):
        for j in range(1,len(string2)):
            # Match
            match_cost = get_match_cost(string1[i], string2[j])
            temp[0] = matrix[i - 1][j - 1] + match_cost
            # Insert
            temp[1] = matrix[i][j - 1] + 1
            # Delete
            temp[2] = matrix[i - 1][j] + 1

            matrix[i][j] = temp[0]
            if(match_cost == 0):
                parent[i][j] = 0
            else:
                parent[i][j] = 3

            for k in range(1, len(temp)):
                if(temp[k] < matrix[i][j]):
                    matrix[i][j] = temp[k]
                    parent[i][j] = k

    result = []
    reconstruct_path(parent, string1, string2, len(string1) - 1, len(string2) - 1, result)
    result.reverse()
    sequence = ("").join(result)
    print(sequence)
    return matrix[len(string1) - 1][len(string2) - 1]

def get_match_cost(char1, char2):
    if(char1 == char2):
        return 0
    return 1

def initialize_matrix(matrix, is_parent):
    if is_parent:
        matrix[0][0] = -1
        for i in range(1, len(matrix)):
            matrix[i][0] = 2
        for i in range(1, len(matrix[0])):
            matrix[0][i] = 1
    else:
        for i in range(len(matrix)):
            matrix[i][0] = i

        for i in range(len(matrix[0])):
            matrix[0][i] = i

def reconstruct_path(parent, string1, string2, i, j, result):
    if(parent[i][j] == 0):
        result.append('M')
        reconstruct_path(parent, string1, string2, i-1, j-1, result)
        return
    elif(parent[i][j] == 1):
        result.append('I')
        reconstruct_path(parent, string1, string2, i, j-1, result)
        return
    elif(parent[i][j] == 2):
        result.append('D')
        reconstruct_path(parent, string1, string2, i-1, j, result)
        return
    elif(parent[i][j] == 3):
        result.append('S')
        reconstruct_path(parent, string1, string2, i-1, j-1, result)
        return
    return
        
# print(edit_distance("thou shalt not", "you should not"))
print(edit_distance("watch the movie raising arizona?", "watch da mets raze arizona?"))
print(edit_distance("this is what happens when I type slow","htishisth whaty havpens when ui type fasht"))
print(edit_distance("leonard skiena","lynard skynard"))

