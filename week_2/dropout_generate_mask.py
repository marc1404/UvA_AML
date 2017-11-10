def choice(p, a, b):
    if np.random.random() < p:
        return a
    else:
        return b


def dropout_generate_mask(shape, drop_rate):
    choice_vectorized = np.vectorize(choice)
    mask = choice_vectorized(drop_rate, np.zeros(shape), np.ones(shape))

    return mask
