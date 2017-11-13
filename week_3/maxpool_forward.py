def maxpool_forward(x_input):
    length_y, length_x = x_input.shape
    axis_y = list(range(length_y))[::2]
    axis_x = list(range(length_x))[::2]
    output = np.zeros((length_y // 2, length_x // 2))

    for y in axis_y:
        for x in axis_x:
            batch = x_input[y:y + 2, x:x + 2]
            output[y // 2][x // 2] = batch.max()

    return output
