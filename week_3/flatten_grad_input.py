def flatten_grad_input(x_input, grad_output):
    k, l, m, n = x_input.shape
    grad_input = np.reshape(grad_output, (k, l, m, n))

    return grad_input
