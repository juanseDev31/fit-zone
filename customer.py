class Customer:
    def __init__(self, id=None, name=None, last_name=None, membership=None):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._membership = membership

    def __str__(self):
        return (f'Id: {self._id}, Name: {self._name}, '
                f'Last Name: {self._last_name}, Membership: {self._membership}')