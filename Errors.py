class InvalidInputError(ValueError):
    """
    raised when the input is incorrect
    """
    pass


class ReservedFieldError(Exception):
    """
    raised when the field is already taken
    """
    pass
