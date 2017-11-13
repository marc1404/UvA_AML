def flatten_forward(x_input):
    k, l, m, m = x_input.shape
    output = np.reshape(x_input, (k, l * m * n))

    return output