# Darius Vaiaoga, Logging In
# Nicholas Larsen, Encrypting Data
from Crypto.Cipher import AES
import base64

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def read_file():

    key = b'Imaginary Elephant Tonsil Spleen'
    nonce = b'12345678'

    with open('profile.txt', 'r') as profile_file:
        profile = profile_file.read().split(',')

    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plain = cipher.decrypt(base64.b64decode(profile[1])).decode()
    profile[1] = plain
    
    return profile

def write_profile(username, password):

    key = b'Imaginary Elephant Tonsil Spleen'
    nonce = b'12345678'

    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode())).decode()


    with open('profile.txt', 'w') as profile_file:
        profile_file.write(f'{username},{password}')

def encrypt(password, key):

    for character in password:
        key += 1

        # If the character is letter, either raise or lower it's case
        if character.lower() in lowercase_letters:
            if key % 2 == 0:
                character = character.lower()
            else:
                character = character.upper()
        # If the character is a number, either add or subtract 1 from it
        elif character in numbers:
            if key % 2 == 0:
                character = str(int(character) + 1)

def login():

    while True:
        # ['_', '_'] is the default

        profile = read_file()

        # IF there is a profile, get user to input username and password
        if profile != ['_', '_']:

            while True:

                username_attempt = str(input('Username: '))
                password_attempt = str(input('Password: '))

                print(username_attempt)
                print(password_attempt)

                if [username_attempt, password_attempt] == profile:
                    print(f'Welcome {username_attempt}.')
                    return True
                else:
                    print('Incorrect Username or Password')
                    continue

        # ELSE if there isn't, get user to create a new profile
        else:
            print('Profile not found.')
            print('Creating new profile...')
            write_profile(input('Enter New Username: '), input('Enter New Password: '))

            # Has user redo process if the username/password if there is an invalid combination
            if read_file() == ['_', '_'] or '' in read_file():
                print('Invalid Input')
                write_profile('_','_')

#login()
