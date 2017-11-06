def dense_grad_b(x_input, grad_output, W, b):
    ones = np.ones_like(grad_output)
    ones_transposed = np.transpose(ones)
    grad_b = np.dot(ones_transposed, grad_output)

    return grad_b
