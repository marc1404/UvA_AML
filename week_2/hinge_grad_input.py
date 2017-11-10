def hinge_grad_input(target_pred, target_true):
    return np.where(target_pred * target_true < 1, 1 / len(target_pred) * -target_true, 0)
