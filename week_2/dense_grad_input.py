def dense_grad_input(x_input, grad_output, W, b):
    W_transposed = np.transpose(W)
    grad_input = np.dot(grad_output, W_transposed)

    return grad_input
