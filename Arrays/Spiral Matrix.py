matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]

min_i = 0
max_i = len(matrix)
min_j = 0
max_j = len(matrix[0])

i = 0
j = 0

k = 0
ele_count = max_i * max_j
output = [0] * ele_count

max_i -= 1
max_j -= 1

while k < ele_count:
    while j <= max_j:
        output[k] = matrix[i][j]
        k += 1
        j += 1
    min_i += 1
    j -= 1
    i += 1

    if k == ele_count:
        break
    
    while i <= max_i:
        output[k] = matrix[i][j]
        k += 1
        i += 1
    max_j -= 1
    i -= 1
    j -= 1

    if k == ele_count:
        break

    while j >= min_j:
        output[k] = matrix[i][j]
        k += 1
        j -= 1
    max_i -= 1
    j += 1
    i -= 1

    if k == ele_count:
        break

    while i >= min_i:
        output[k] = matrix[i][j]
        k += 1
        i -= 1
    min_j += 1
    i += 1
    j += 1

    if k == ele_count:
        break


print(output)
