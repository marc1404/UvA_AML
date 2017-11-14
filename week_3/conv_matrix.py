def conv_matrix(matrix, kernel):
    output = np.ndarray(shape=matrix.shape)
    matrix_height, matrix_width = matrix.shape
    kernel_height, kernel_width = kernel.shape
    padding_x = kernel_width // 2
    padding_y = kernel_height // 2
    padded = np.pad(matrix, [(padding_y, padding_y), (padding_x, padding_x)], 'constant', constant_values=0)

    for y in range(matrix_height):
        for x in range(matrix_width):
            batch = padded[y:y + kernel_height, x:x + kernel_width]
            multiplied = batch * kernel
            output[y][x] = np.sum(multiplied)

    return output
