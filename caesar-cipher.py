#!/usr/bin/python
# Caesar Cipher Encryption, Decryption, & Bruteforcing
# Created By : C0SM0

# symbols and characters that can't be proccessed through the algorithm
symbols = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']


# output files
encrypted_file = 'encrypted-caesar.txt'
decrypted_file = 'decrypted-caesar.txt'
bruteforce_all_file = 'bruteforce-all-keys.txt'
bruteforce_range_file = 'bruteforce-range.txt'

# writes output to file
def write_file(output_file, output_text):
    # write to file
    with open(output_file, 'w')as f:
        f.write(output_text)
        print(f'Success! Output Written to {output_file}')

# translator, encrypts and decrypts files
def translator(file, translate):
    text = ''
    output_text = ''

    # create shift
    shift = int(input('\nShift of : '))

    # encrypt or decrypt depending on translate option
    print('Translating...')
    for letter in file:

        # encrypt, option 1
        if translate == '1':
            output_file = encrypted_file
            if letter in symbols:
                text += letter
            elif letter.isupper():
                text += chr((ord(letter) + shift - 65) % 26 + 65)
            else:
                text += chr((ord(letter) + shift - 97) % 26 + 97)

        # decrypt, option 2
        elif translate == '2':
            output_file = decrypted_file
            if letter in symbols:
                text += letter
            elif letter.isupper():
                text += chr((ord(letter) - shift - 65) % 26 + 65)
            else:
                text += chr((ord(letter) - shift - 97) % 26 + 97)

        # exception
        else:
            print('Invalid Translate Option, Try Again!\n')
            break

    # removes extra character from encryption method
    if translate == '1':
        text_length = len(text)
        for num in range(0, text_length):
            if num != text_length -1:
                output_text += text[num]

    else:
        output_text = text

    write_file(output_file, output_text)

# bruteforces files
def bruteforce(file):
    text = ''
    bruteforce_option = input('\nChoose an Option :\n1) Bruteforce All shift Keys\n2) Choose Range\n')

    # all shift keys, option 1
    if bruteforce_option == '1':
        start_range = 0
        end_range = 27
        output_file = bruteforce_all_file

    # choose range, option 2
    elif bruteforce_option == '2':
        start_range = int(input('\nStart Range : '))
        end_range = int(input('End Range : '))
        output_file = bruteforce_range_file

    # exception
    else:
        print('Input Not Recognized, Try Again!\n')

    # bruteforce, option 3
    print('Bruteforcing...')
    shift_key = start_range
    for shift in range(start_range, end_range):
        text += f'Shift Key: {shift_key}\n'
        shift_key += 1

        for letter in file:
            if letter in symbols:
                text += letter
            elif letter.isupper():
                text += chr((ord(letter) - shift - 65) % 26 + 65)
            else:
                text += chr((ord(letter) - shift - 97) % 26 + 97)

        text += '\n\n'

    write_file(output_file, text)

# main code
def caesar_main():

    # user input
    while True:
        input_file = input('Enter File Name : ')

        # read input file
        try:
            with open(input_file, 'r') as f:
                read_file = f.read()

        except FileNotFoundError:
            print('File Does Not Exist, Try Again!\n')
            break

        # user input, options
        option = input('Choose an Option :\n1) Encrypt\n2) Decrypt\n3) Bruteforce\n4) Exit\n')

        # encrypt option
        if option == '1':
            translator(read_file, option)
            break

        # decrypt option
        elif option == '2':
            translator(read_file, option)
            break

        # bruteforce option
        elif option == '3':
            bruteforce(read_file)
            break

        # exit option
        elif option == '4':
            print('Exiting...')
            break

        # exception
        else:
            print('Inptut Was Not Recognized, Try Again!\n')
            break

if __name__ == "__main__":
    caesar_main()
