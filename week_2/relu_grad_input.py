def relu_grad_input(x_input, grad_output):
    return np.where(x_input > 0, 1, 0) * grad_output
