"""
Create a function that reverses a string:
'Hi My name is yoosseck' should be:
'kcessooy si eman yM iH
"""


def reverse(param):

    if (len(param) < 2 or isinstance(param, str)):
        raise Exception('''
                        The input should be either is
                        equal to or more than
                        2 characters, and should be a value of string
                        ''')
    result = ''
    for char in reversed(param):
        result += char

    return result


if __name__ == "__main__":
    print('start:')
    output = reverse(param='Hi My name is yoosseck')
    print(output)
    output = reverse(param=124)
