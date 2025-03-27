def read_file():
    with open('profile.txt', 'r') as profile_file:
        profile = profile_file.read().split(',')

    return profile

def write_profile(username, password):
    with open('profile.txt', 'w') as profile_file:
        profile_file.write(f'{username},{password}')

def login():

    while True:
        # ['_', '_'] is the default

        profile = read_file()

        # IF there is a profile, get user to input username and password
        if profile != ['_', '_']:

            while True:

                username_attempt = input('Username: ')
                password_attempt = input('Password: ')

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
