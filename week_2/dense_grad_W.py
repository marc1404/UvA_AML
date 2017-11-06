def dense_grad_W(x_input, grad_output, W, b):
    x_transposed = np.transpose(x_input)
    grad_W = np.dot(x_transposed, grad_output)

    return grad_W
