"""
A7 - 1: DICTIONARIES
"""

__author__ = 'Hossain, Sadman'


def get_data(type) -> str:
    """Return string input from user."""

    while True:
        data = input('Enter a {}: '.format(type))
        if data != '':
            return data
        print("Invalid {}. Try again.".format(type))


def get_type() -> str:
    """Return string input from user if input is a supported data type (str, 
    int, float, bool) or an empty string."""

    while True:
        type = input('Enter its type: ')
        if type in ['','str','int','float','bool']:
            return type
        print("Invalid type. Try again.")


def cast(data):
    """Convert data string to a user-inputted data type (str, int, float, bool, 
    None)."""

    while True:
        type = get_type()
        try:
            if type == 'int':
                data = int(data)
            elif type == 'float':
                data = float(data)
            elif type == 'bool':
                data = bool(data)
            elif type == '':
                data = None
        except ValueError:
            print('Invalid type. Try again.')
            continue
        return data


def main():
    dict = {}
    while True:
        key = cast(get_data('key'))
        if key == None:
            break
        value = cast(get_data('value'))
        if value == None:
            break
        dict[key] = value
    print(dict)


if __name__ == '__main__':
    main()