from waterfall.secret_space import SecretSpace


def select_phase(picture, phase):
    assert phase in picture.phases
    phases = dict()
    for f in picture.phases:
        phases[f] = getattr(picture, f)

    secret_space = SecretSpace(getattr(picture, phase))

    def revert(secret_space):
        phases[phase] = secret_space
        return type(picture).from_phases(**phases)
    setattr(secret_space, 'revert', revert)

    return secret_space
