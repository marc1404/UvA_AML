def hinge_grad_input(target_pred, target_true):
    return np.negative(target_true) / len(target_true)
