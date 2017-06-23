from .check_types import *
from distutils.util import strtobool


def load_parameters(parameters_file_path):

    parameters = {}

    parameters_file = open(parameters_file_path)

    for i, line in enumerate(parameters_file):
        if line:
            temp = line[:-1].split(' = ')
            if len(temp) != 2:
                print('Error while loading parameters: line ' + str(i) + '\n')
                print('"' + line + '"' + '\n')
                return None
            else:
                value = temp[1]
                if is_int(temp[1]):
                    value = int(temp[1])
                elif is_float(temp[1]):
                    value = float(temp[1])
                elif is_bool(temp[1]):
                    value = strtobool(temp[1])
                parameters[temp[0]] = value

    return parameters
