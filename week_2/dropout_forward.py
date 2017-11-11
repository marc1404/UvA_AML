def dropout_forward(x_input, mask, drop_rate, training_phase):
    if training_phase:
        return x_input * mask
    else:
        return x_input * (1 - drop_rate)
