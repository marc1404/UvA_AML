def l2_regularizer(weight_decay, weights):
    return weight_decay / 2 * np.sum(np.square(weights))
