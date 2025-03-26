def read_file():
    with open('profile.txt', 'r') as profile_file:
        profile = profile_file.read().split(',')

    return profile

def login():

    while True:
        # ['_', '_'] is the default

        profile = read_file()

        if profile != ['_', '_']:

            while True:

                username_attempt = input('Username: ')
                password_attempt = input('Password: ')

                if [username_attempt, password_attempt] == profile:
                    return True
                else:
                    print('Incorrect Username or Password')
                    continue
        
