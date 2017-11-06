# TODO: Rewrite using NumPy functions
def hinge_forward(target_pred, target_true):
    sum = 0;

    for pred_row, true_row in zip(target_pred, target_true):
        for pred, truth in zip(pred_row, true_row):
            sum += np.maximum(0, 1 - pred * truth)

    output = sum / len(target_pred)

    return output
