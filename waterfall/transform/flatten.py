from waterfall.secret_space import SecretSpace


def flatten(space):
    shape = space.shape

    secret_space = SecretSpace(space.flatten())

    def revert(secret_space):
        return space.revert(secret_space.reshape(shape))
    secret_space.revert = revert

    return secret_space
