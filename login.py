import os

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def read_file():
    with open('profile.txt', 'r') as profile_file:
        profile = profile_file.read().split(',')

    return profile

def write_profile(username, password):
    with open('profile.txt', 'w') as profile_file:
        profile_file.write(f'{username},{password}')

def login():

    os.environ['PYTHONHASHSEED']='0'

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

login()
