def box_blur(image, box_size):
    kernel = np.ones((box_size, box_size))
    kernel /= np.square(box_size)
    output = conv_matrix(image, kernel)

    return output
