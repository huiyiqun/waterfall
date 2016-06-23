class SecretSpace(object):
    def __init__(self, array):
        self._array = array

    def __getattr__(self, attr):
        if attr != 'revert':
            return getattr(self._array, attr)

    def __getitem__(self, key):
        return self._array[key]

    def __setitem__(self, key, value):
        self._array[key] = value

    def __len__(self):
        return len(self._array)
