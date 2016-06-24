from pywt import dwt2, idwt2

from waterfall.secret_space import SecretSpace


def dwt(space):
    assert space.ndim == 2

    cA, (cH, cV, cD) = dwt2(space, 'db1')
    secret_space = SecretSpace(cH.astype(int))

    def revert(secret_space):
        return space.revert(
            idwt2((cA, (secret_space[:], cV, cD)), 'db1').astype(int))
    secret_space.revert = revert

    return secret_space
