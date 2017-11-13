def conv_matrix(matrix, kernel):
    output = np.zeros_like(matrix)
    kernel_center = len(kernel) // 2
    padded = np.pad(matrix, kernel_center, 'constant', constant_values=0)

    for (y, row) in enumerate(matrix):
        for (x, value) in enumerate(row):
            end_x = x + kernel_center * 2 + 1
            end_y = y + kernel_center * 2 + 1
            batch = padded[y:end_y, x:end_x]
            multiplied = batch * kernel
            output[y][x] = np.sum(multiplied)

    return output
