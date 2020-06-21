'''
EasyCrypt Text Encryptor/Decryptor
'''

__author__ = 'J Che', 'S Hossain'


from random import randint


def generate_menu():
    """Return a string containing the menu displaying options for encryption 
    program.

    >>> generate_menu()
    "Please choose from one of the following menu options:
    1. Encrypt plaintext.
    2. Decrypt ciphertext.
    3. Generate key.
    4. Exit."
    """
    menu = ""
    menu += "Please choose from one of the following menu options:\n"
    menu += "1. Encrypt plaintext.\n"
    menu += "2. Decrypt ciphertext.\n"
    menu += "3. Generate key.\n"
    menu += "4. Exit.\n"
    return menu


def print_title(msg):
    """Prints msg with hyphens as long as msg on the line above and below.

    >>> print_title("EasyCrypt Text Encryptor/Decryptor")
    ----------------------------------
    EasyCrypt Text Encryptor/Decryptor
    ----------------------------------
    >>> print_title("A")
    -
    A
    -
    """
    line = "-" * len(msg)
    print(line)
    print(msg)
    print(line)


def get_int(msg, error_msg, out_of_bounds_msg, lower, upper):
    """Gets integer input from user after displaying msg.

    If exception ValueError is encountered or input is outside of bounds (between
    1 and upper, inclusive), error_msg or out_of_bounds_msg is displayed
    respectively and input is taken again (until an integer within the declared
    bounds is inputted).

    >>> get_int("Input message: ", "Error message.", "Out of bounds message.", 4)
    Input message: 5
    Out of bounds message.
    >>> get_int("Input message: ", "Error message.", "Out of bounds message.", 4)
    Input message: abcde
    Error message.
    >>> get_int("Input message: ", "Error message.", "Out of bounds message.", 4)
    Input message: 2
    """
    while True:
        try:
            num = int(input(msg))
            if lower <= num <= upper:
                return num
            else:
                print(out_of_bounds_msg)
                continue
        except ValueError:
            print(error_msg)
            continue


def clean_text(input_text):
    """Return string with all non-alphabetic characters in input_text removed and all 
    letters converted to uppercase.

    >>> clean_text("A1b2CD")
    "ABCD"
    >>> clean_text("1234")
    ""
    """
    text = ""
    for char in input_text:
        #  .isalpha() checks if each character is a letter
        if char.isalpha():
            text += char
    text = text.upper()
    return text


def get_text(msg, error_msg, bounded, lower, upper):
    """Gets string input from user after displaying msg, with all alphabetic 
    characters converted to uppercase and all non-alphabetic characters stripped
    from input.

    If string input has length outside of bounds (inclusive) and bounded is true, 
    then "invalid length" is displayed and string input is taken again (until a 
    valid string input within the length bounds is received).

    >>> get_text("Input message: ", "Error message.", False)
    Input message: example text
    >>> get_text("Input message: ", "Error message.", True)
    Input message: 
    Error message.
    >>> get_text("Input message: ", "Error message.", False)
    Input message: 
    """
    while True:
        text = input(msg)
        if bounded and not (lower <= len(clean_text(text)) <= upper):
            print(error_msg)
            continue
        return text


def to_text_list(text):
    """Returns a list of strings with text divided into strings of length 5.

    If text does not have a length of multiple 5, the last string in the list of
    strings will have a length between 1 and 4, inclusive.
    
    >>> plaintext_list("ABCDEFGHIJ")
    ["ABCDE", "FGHIJ"]
    >>> plaintext_list("ABCDEFGHIJKL")
    ["ABCDE", "FGHIJ", "KL"]
    """
    string_list = []
    tmp_string = ""

    for i in range(len(text)):
        tmp_string = tmp_string + text[i]
        #  once tmp_string reaches length of 5, it is appended to list of strings 
        if len(tmp_string) == 5:
            string_list.append(tmp_string)
            tmp_string = ""
    
    #  if tmp_string has fewer than 5 characters, it will not be appended in for
    #  loop above but still contains characters from text, and so it is appended
    #  to list of strings below.
    if not len(tmp_string) == 0:
        string_list.append(tmp_string)
    
    return string_list


def to_text(lst):
    """Returns a string containing strings in lst concatenated together a space
    between strings.

    >>> to_text(["ABCDE", "FGHIJ"])
    "ABCDEFGHIJ"
    >>> ["ABCDE", "FGHIJ", "KL"]
    "ABCDEFGHIJKL"
    """
    text = ""
    for i in range(len(lst)):
        #  if the last string in lst is being concatenated, there will be no space
        #  concatenated to the text string
        if i == len(lst):
            text += lst[i]
            break
        text += lst[i] + " "
    return text


def get_alpha_position_list(key):
    """Returns a list of integers, with each integer corresponding to the 
    alphabetic position of each letter in key

    >>> get_alpha_position_list("ABCDE")
    [1, 2, 3, 4, 5]
    >>> get_alpha_position_list("ZF")
    [26, 6]
    """
    key_list = to_text_list(key)
    alpha_position_list = []
    for letter in key:
        # each letter in key is converted to its ascii value and subtracted by 64,
        # which is the number of elements before 'A' in the ascii table
        alpha_position_list.append(ord(letter) - 64)
    return alpha_position_list


def encrypt_codec(text, key, encrypt):
    """Return a list of strings each length 5 (potentially excluding last item)
    with text encrypted (if encrypt == True) or text decrypted (if encrypt == False)
    using key.

    >>> encryption_codec("ABCDE", “A”, True)
    “BCDEF”
    >>> encryption_codec("GOOSFRABAA", “ANGRMNGMT”, False)
    “FAHAS DTOGZ”
    """
    #  convert text to a list of strings each 5 characters long (except last item)
    #  if text has length that is not a multiple of 5
    text_list = to_text_list(text)
    #  get list of integers using key that represent the value by which to 
    #  shift (encrypt or decrypt) each letter in text
    key_list = get_alpha_position_list(key)

    output = []
    tmp_string = ""
    key_index = 0

    #  iterate through each string in text_list
    for i in range(len(text_list)):
        #  assign string at index i to a temporary string variable
        block = text_list[i]
        #  iterate through each character in temporary string block
        for j in range(len(block)):
            #  if encrypting, add the current value in key_list to the 
            #  ascii value of character j to get encrypted ascii value
            if encrypt:
                mutated_ascii = ord(block[j]) + key_list[key_index]
            #  if decrypting, subtract the current value in key_list to the 
            #  ascii value of character j to get decrypted ascii value
            else:
                mutated_ascii = ord(block[j]) - key_list[key_index]

            #  if encrypted or decrypted (mutated) ascii value is above or below 
            #  bounds of uppercase letters (65 to 90, inclusive) in ascii table,
            #  subtract or add 25 respectively  
            if mutated_ascii > 90:
                mutated_ascii -= 26
            elif mutated_ascii < 65:
                mutated_ascii += 26

            #  append the character value of mutated ascii to tmp_string
            tmp_string += chr(mutated_ascii)
            
            #  once tmp_string reaches length 5, append tmp_string to output
            #  and assign tmp_string to be empty
            if len(tmp_string) == 5:
                output.append(tmp_string)
                tmp_string = ""

            #  increment key_index by 1 to iterate through each integer in key_list
            #  for each letter in text
            key_index += 1
            #  if key_index reaches length of key, set key_index to 0 to reiterate
            #  through key_list
            if key_index == len(key):
                key_index = 0

    #  if encrypting and the length of block (last string in text_list) has length
    #  less than 5, then append next characters from key starting at index 
    #  key_index until length of tmp_string is 5
    if encrypt and len(tmp_string) < 5:
        while len(tmp_string) < 5:
            tmp_string += key[key_index]

            key_index += 1
            if key_index == len(key):
                key_index = 0 
        #  once tmp_string has reached length of 5, append to output
        output.append(tmp_string)
    #  if decrypting, append tmp_string to output in case of block not having
    #  length of 5
    elif not encrypt:
        output.append(tmp_string)

    return output


def generate_key(length):
    """Returns a string of random uppercase letters that is length letters long.

    >>> generate_key(2)
    "JD"
    >>> generate_key(10)
    "SUIFAUFHUE"
    """
    key = ""
    for i in range(length):
        #  append the character correspnding to a random ascii integer between
        #  65 and 90 (inclusive)
        key += chr(randint(65,90))
    return key


def program_service():
    """Runs primary methods of encryptor program, including displaying menu, 
    getting input, and running specific encryptor program submethods based on 
    user input.
    """
    MENU = generate_menu()
    while True:
        print(MENU)
        option = get_int("> ", "\nInvalid choice. Try again.\n\n" + MENU, "\nInvalid choice. Try again.\n\n" + MENU, 1, 4)
        print("")
        if option == 1:
            encryption_service()
        elif option == 2:
            decryption_service()
        elif option == 3:
            generate_key_service()
        elif option == 4:
            break


def encryption_service():
    """Runs submethod for encrypting plaintext input from user based on inputted
    plaintext and encryption key.

    Receiving input from user, printing inputs, and printing encrypted text for the
    encryption service occur inside this function.
    """
    text = clean_text(get_text("Please enter text to encrypt: ", "", False, 0, 0))
    print("This is the plaintext: " + to_text(to_text_list(text)) + "\n")

    key = clean_text(get_text("A key is any string of letters (1-1000 chars): ", "invalid length", True, 1, 1000))
    print("Using encryption key: " + key)
    
    print("\nYour message has been encrypted: \n" + to_text(encrypt_codec(text, key, True)) + "\n")


def decryption_service():
    """Runs submethod for decrypting ciphertext input from user based on inputted
    ciphertext and encryption key.

    Receiving input from user, printing inputs, and printing decrypted text for the
    decryption service occur inside this function.
    """
    text = clean_text(get_text("Please enter text to decrypt: ", "", False, 0, 0))
    print("This is the ciphertext: " + to_text(to_text_list(text)) + "\n")
    
    key = clean_text(get_text("A key is any string of letters (1-1000 chars): ", "invalid length", True, 1, 1000))
    print("Using decryption key: " + key)
    
    print("\nYour message has been decrypted:\n" + to_text(encrypt_codec(text, key, False)) + "\n")


def generate_key_service():
    """Runs submethod for generating a random key of length inputted by user.

    Receiving input from user, printing inputs, and printing generated key 
    occur inside this function.
    """
    print("Generate an encryption key comprised of random characters (max 1000).")
    key_length = get_int("Enter the desired length of key (1-1000): ", "not an integer", "invalid", 1, 1000)
    print("Your new encryption key: \n" + generate_key(key_length) + "\n") 


def main():
    print_title("EasyCrypt Text Encryptor/Decryptor")
    print("")
    program_service()


if __name__ == '__main__':
    main()