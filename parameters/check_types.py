import os
from distutils.util import strtobool


def is_int(value):
    """
    Verifies that 'value' is an integer.
    """
    try:
        int(value)
    except ValueError:
        return False
    else:
        return True


def is_float(value):
    """
    Verifies that 'value' is a float.
    """
    try:
        float(value)
    except ValueError:
        return False
    else:
        return True


def is_str(value):
    """
    Verifies that 'value' is a string.
    """
    if not type(value) is str:
        return False
    else:
        return True


def is_bool(value):
    """
    Verifies that 'value' is a boolean.
    """
    try:
        strtobool(value)
    except ValueError:
        return False
    else:
        return True


def is_dir(value):
    """
    Verifies that 'value' is a path to an existing directory.
    """
    if not (type(value) is str and os.path.isdir(value)):
        return False
    else:
        return True


def is_file_i(value):
    """
    Verifies that 'value' is a path to an existing file.
    """
    if not (type(value) is str and os.path.isfile(value)):
        return False
    else:
        return True


def is_file_o(value):
    """
    Verifies that 'value' is a path to a valid directory to create an output
    file.
    """
    if not (type(value) is str and os.path.split(value)[0]):
        return False
    else:
        return True
