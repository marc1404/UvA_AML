def dense_forward(x_input, W, b):
    dot = np.dot(x_input, W)
    output = np.add(dot, b)

    return output
