def conv_matrix(matrix, kernel):
    output = np.ndarray(shape=matrix.shape)
    kernel_height, kernel_width = kernel.shape
    x_offset = kernel_width // 2
    y_offset = kernel_height // 2
    padding = np.maximum(x_offset, y_offset)
    padded = np.pad(matrix, padding, 'constant', constant_values=0)

    for (y, row) in enumerate(matrix):
        for (x, value) in enumerate(row):
            start_x = x + padding - x_offset
            start_y = y + padding - y_offset
            end_x = x + padding + 1 + x_offset
            end_y = y + padding + 1 + y_offset
            batch = padded[start_y:end_y, start_x:end_x]
            multiplied = batch * kernel
            output[y][x] = np.sum(multiplied)

    return output
